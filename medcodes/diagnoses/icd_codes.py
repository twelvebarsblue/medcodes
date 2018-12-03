from _mappers import charlson_matches_codes, charlson_startswith_codes

def charlson_comorbidities(icd_code, icd_version=9):
    """
    Outputs Charlson comorbidity for a given ICD code.

    Parameters
    ----------
    code : str
        ICD code
    icd_version : str
        Can be either 9 or 10

    Returns
    -------
    Charlson comorbidity

    References
    ----------
    [1] Quan H, Sundararajan V, Halfon P, et al. Coding algorithms for defining Comorbidities in ICD-9-CM
    and ICD-10 administrative data. Med Care. 2005 Nov; 43(11): 1130-9.
    """
    if not isinstance(icd_code, str):
        raise TypeError("ICD code must be a string.")

    icd_code = icd_code.replace(".", "")
    icd_code = icd_code.strip()

    comorbidity = None
    for k, val in charlson_matches_codes.items():
        if icd_code in val:
            comorbidity = k
    if comorbidity is None:
        for k, val in charlson_startswith_codes.items():
            if icd_code.startswith(tuple(val)):
                comorbidity = k
    return comorbidity

def elixhauser_comorbidities(icd_code, icd_version=9):
    """
    Outputs Elixhauser comorbidity for a given ICD code.

    Parameters
    ----------
    code : str
        ICD code
    icd_version : str
        Can be either 9 or 10
    
    Returns
    -------
    Elixhauser comorbidity
    """
    pass