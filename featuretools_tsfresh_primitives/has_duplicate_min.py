from tsfresh.feature_extraction.feature_calculators import has_duplicate_min

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Numeric


class HasDuplicateMin(AggregationPrimitive):
    """
    Checks if the maximum value of x is observed more than once.
    """
    name = "has_duplicate_min"
    input_types = [Numeric]
    return_type = Numeric
    stack_on_self = False

    def get_function(self):
        return has_duplicate_min
