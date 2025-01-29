
def cigar_party(cigars, is_weekend):
  if is_weekend and cigars >= 40:
    return True
  elif is_weekend == False and (60 >= cigars >= 40):
    return True
  else:
    return False

