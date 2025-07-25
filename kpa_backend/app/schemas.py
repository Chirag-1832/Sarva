from pydantic import BaseModel
from datetime import date
from typing import Optional, List, Dict,Any

class WheelFields(BaseModel):
    treadDiameterNew: str
    lastShopIssueSize: str
    condemningDia: str
    wheelGauge: str
    variationSameAxle: str
    variationSameBogie: str
    variationSameCoach: str
    wheelProfile: str
    intermediateWWP: str
    bearingSeatDiameter: str
    rollerBearingOuterDia: str
    rollerBearingBoreDia: str
    rollerBearingWidth: str
    axleBoxHousingBoreDia: str
    wheelDiscWidth: str


class WheelSpecificationCreate(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: date
    fields: WheelFields

class WheelSpecListResponse(BaseModel):
    success: bool 
    message: str 
    data: List[Any] | Dict[str, Any]


    class Config:
        orm_mode = True

