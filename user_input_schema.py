# suer input pydantic model
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated

class UserInput(BaseModel):
    # model attributes
    age: Annotated[int, Field(..., gt = 0, le = 100, description="Patient age should be less than 100")]
    sex: Annotated[Literal["male", "female"], Field(..., description="Patient gender (male or female)")]
    bmi: Annotated[float, Field(..., gt=0.0, description = "Patient of BMI")]
    children: Annotated[int, Field(..., gt = 0, description = "No of children a patient has")]
    smoker: Annotated[bool, Field(..., description = "Is Patient a smoker? (yes/no)")]
    region: Annotated[Literal['southwest', 'southeast', 'northwest', 'northeast'], 
                      Field(..., description = "Select a region name a patient belongs to")]

    @computed_field
    @property
    def sex_int(self) -> int:
        # 1 for male gender
        return 1 if (self.sex == "male") else 0
    
    @computed_field
    @property
    def smoker_int(self) -> int:
        # 1 for smoker(true) 0 for non-smoker
        return 1 if (self.smoker == True) else 0

    @computed_field
    @property
    def region_int(self) -> int:
        if self.region == "southwest":
            return 0
        
        elif self.region == "southeast":
            return 1
        
        elif self.region == "northwest":
            return 2
        
        else:
            return 3