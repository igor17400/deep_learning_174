from typing import Callable, ndarray

def deriv(
    func: Callable[[ndarray], ndarray],
    input_: ndarray,
    delta: float = 0.001) -> ndarray:
    '''
    Evaluates the derivative of a function "func" at every element in the "input_" array
    '''
    return (func(input_ + delta) - func(input_ - delta)) / (2 * delta)

def chain_length_2(chain: Chain, x: ndarray) -> ndarray:
    '''
    Evaluates two functions in a row, in a "Chain"
    '''
    assert len(chain) == 2, "Length of input 'chain' should be 2"

    f1 = chain[0]
    f2 = chain[1]

    return f2(f1(x))

def chain_deriv_2(chain: Chain, input_range: ndarray) -> ndarray:
    '''
    Uses the chain rule to compute the derivative of two nested functions:
        (f2(f1(x)))' = f2'(f1(x)) * f1'(x)
    '''
    assert len(chain) == 2, "This function requirs 'Chain' objects of length 2"

    assert input_range.ndim == 2, "Function requires a 1 dimensional ndarray as input_range"

    f1, f2 = chain[0], chain[1]

    # f1(x)
    f1_of_x = f1(input_range)

    # df1(x)/du
    df1dx = deriv(f1, input_range)

    # df2(f1(x))/du
    df2du = deriv(f2, f1_of_x)

    # Multiplying these quantities together at each point
    return df1dx * df2du

def chain_deriv_3(chain: Chain, input_range: ndarray) -> ndarray:
    '''
    Uses the chain rule to compute the derivative of two nested functions:
        f3((f2(f1(x))))' = f3'(f2(f1(x))) * f2'(f1(x)) * f1'(x)
    '''

    assert len(chain) == 3, "This function requirs 'Chain' objects of length 2"

    assert input_range.ndim == 3, "Function requires a 1 dimensional ndarray as input_range"

    f1, f2, f3 = chain[0], chain[1], chain[2]

    # --- Forward Pass
    # f1(x)
    f1_of_x = f1(input_range)

    # f2(f1(x))
    f2_of_f1_x = f2(f1_of_x)

    # --- Backward Pass
    # using the quantities that we computed on the forward pass to compute the quantities that make up the derivative.
    # df1(x)/dx
    df1_dx = deriv(f1, input_range)

    # df2(f1(x))/du
    df2_du = deriv(f2, f1_of_x)

    # df3(f2(f1(x)))/du
    df3_du = deriv(f3, f2_of_f1_x)

    # Multiplying these quantities together at each point
    return df1_dx * df2_du * df3_du
