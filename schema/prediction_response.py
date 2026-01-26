from pydantic import BaseModel,Field
from typing import Dict



class PredictionResponse(BaseModel):
    predicted_category:str=Field(...,description="The predicted insurance premium category",example="Low")
    confidence:float=Field(...,description="Model's confidence score for the predicted class (range: 0 to 1 )",example=0.2)
    class_probabilities:Dict[str,float] = Field(...,description="Probability distribution across all possible classes",example={"Low":0.1,"Medium":0.1,"High":0.3})
    