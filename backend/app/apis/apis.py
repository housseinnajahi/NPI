import csv

from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from fastapi import HTTPException

from .. import models, schemas, utils
from ..postgres import postgres

router = APIRouter(prefix="")


@router.post("/calculate/", response_model=schemas.CalculationResponse)
def calculate(
    request: schemas.CalculationRequest, db: Session = Depends(postgres.get_db)
):
    try: 
        result = utils.evaluate_npi(request.expression)
        calculation = models.Calculation(
            expression=", ".join(request.expression), result=result
        )
        db.add(calculation)
        db.commit()
        db.refresh(calculation)
        return {"expression": request.expression, "result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/export/")
def export(db: Session = Depends(postgres.get_db)):
    data = db.query(models.Calculation).all()
    filename = "calculations.csv"

    with open(filename, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Expression", "Result"])
        for row in data:
            writer.writerow([row.id, row.expression, row.result])

    return FileResponse(path=filename, media_type="text/csv", filename=filename)
