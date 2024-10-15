from .helpers.weight import WeightCalculator
from .helpers.not_in_use_equations import HarrisBenedictEqs
from .helpers import type_alias

def construct(data: dict[str,
                        type_alias.number]) -> dict[str,
                                                    type_alias.number]:
    data = data.copy()
    weight_calculator = WeightCalculator(weight_initial=data["weight"],
                                        time=data["time"])
    weight_loss_projection = weight_calculator.weight_loss_projection()
    
    data.update(weight_calculator.jsonable_results())

    basal_metabolic_rate = HarrisBenedictEqs(weight_projection=weight_loss_projection,
                                            heihgt=data["height"],
                                            age=data["age"])
    basal_metabolic_rate.for_men()

    data.update(basal_metabolic_rate.jsonable_results())

    return data