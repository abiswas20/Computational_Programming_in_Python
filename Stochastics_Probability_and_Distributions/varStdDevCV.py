def variance(X):
    """Assumes that X is a list of numbers.
    Returns the variance of X."""
    mean=sum(X)/len(X)
    total=0.0
    for i in X:
        total+=(mean-i)**2
    return total/len(X)


def stdDev(X):
    """Assumes that X is a list of numbers.
    Returns the standard deviation of X."""
    return variance(X)**0.5


def CV(X):      #Coefficient of Variation#
    """Assumes that X is a list of numbers.
    Returns the coefficient of variation of X."""
    mean=sum(X)/len(X)
    try:
        return stdDev(X)/mean
    except ZeroDivisionError:
        return float('nan')
