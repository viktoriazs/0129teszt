import fuggvenyek


def cigar_party_teszt2():

    cigar_list = [35, 45, 70, 40, 60]
    is_weekend_lista = [False, False, True, True]
    vart_lista = [False, True, True, False]
    for i in range(0, len(cigar_list)+1):
        print(f"{i+1}. testeset")
        cigars = 34
        is_weekend = is_weekend_lista[i]
        vart = vart_lista[i]
        kapott = fuggvenyek.cigar_party(cigars, is_weekend)
        print(f"cigaretta szama: {cigars} \n"
              f"hetvege e: {is_weekend} \n"
              f"Vart eredemeny: {vart} \n"
              f"kapott: {kapott}\n"
              f"JO_E?: {vart == kapott}\n")


def cigar_party_teszt():
    """Ez tratalmaza a teszteket
    unit testek = egysegteszt - fu"""

    print("1. testeset")
    cigars = 34
    is_weekend = False
    vart  = False
    kapott = fuggvenyek.cigar_party(cigars, is_weekend)
    print(f"cigaretta szama: {cigars} \n"
          f"hetvege e: {is_weekend} \n"
          f"Vart eredemeny: {vart} \n"
          f"kapott: {kapott}\n"
          f"JO_E?: {vart == kapott}\n")

    print("2. testeset")
    cigars = 50
    is_weekend = False
    vart = True
    kapott = fuggvenyek.cigar_party(cigars, is_weekend)
    print(
        f"cigaretta szama: {cigars}\n"
        f"hetvege e: {is_weekend} \n"
        f"Vart eredemeny: {vart}\n"
        f"kapott: {kapott} \n"
        f"JO_E?: {vart == kapott}\n")


    print("3. testeset")
    cigars = 35
    is_weekend = True
    vart = False
    kapott = fuggvenyek.cigar_party(cigars, is_weekend)
    print(
        f"cigaretta szama: {cigars}\n"
        f"hetvege e: {is_weekend} \n"
        f"Vart eredemeny: {vart}\n"
        f"kapott: {kapott} \n"
        f"JO_E?: {vart == kapott}\n")

    print("4. testeset")
    cigars = 45
    is_weekend = True
    vart = True
    kapott = fuggvenyek.cigar_party(cigars, is_weekend)
    print(
        f"cigaretta szama: {cigars}\n"
        f"hetvege e: {is_weekend} \n"
        f"Vart eredemeny: {vart}\n"
        f"kapott: {kapott} \n"
        f"JO_E?: {vart == kapott}\n")

    print("5. testeset")
    cigars = 70
    is_weekend = True
    vart = True
    kapott = fuggvenyek.cigar_party(cigars, is_weekend)
    print(
        f"cigaretta szama: {cigars}\n"
        f"hetvege e: {is_weekend} \n"
        f"Vart eredemeny: {vart}\n"
        f"kapott: {kapott} \n"
        f"JO_E?: {vart == kapott}\n")

    print("6. testeset")
    cigars = 40
    is_weekend = True
    vart = True
    kapott = fuggvenyek.cigar_party(cigars, is_weekend)
    print(
        f"cigaretta szama: {cigars}\n"
        f"hetvege e: {is_weekend} \n"
        f"Vart eredemeny: {vart}\n"
        f"kapott: {kapott} \n"
        f"JO_E?: {vart == kapott}\n")


    print("6. testeset")
    cigars = 60
    is_weekend = True
    vart = True
    kapott = fuggvenyek.cigar_party(cigars, is_weekend)
    print(
        f"cigaretta szama: {cigars}\n"
        f"hetvege e: {is_weekend} \n"
        f"Vart eredemeny: {vart}\n"
        f"kapott: {kapott} \n"
        f"JO_E?: {vart == kapott}\n")


    print("7. testeset")
    cigars = 36
    is_weekend = False
    vart = False
    kapott = fuggvenyek.cigar_party(cigars, is_weekend)
    print(
        f"cigaretta szama: {cigars}\n"
        f"hetvege e: {is_weekend} \n"
        f"Vart eredemeny: {vart}\n"
        f"kapott: {kapott} \n"
        f"JO_E?: {vart == kapott}\n")


    print("8. testeset")
    cigars = 45
    is_weekend = False
    vart = True
    kapott = fuggvenyek.cigar_party(cigars, is_weekend)
    print(
        f"cigaretta szama: {cigars}\n"
        f"hetvege e: {is_weekend} \n"
        f"Vart eredemeny: {vart}\n"
        f"kapott: {kapott} \n"
        f"JO_E?: {vart == kapott}\n")


    print("9. testeset")
    cigars = 70
    is_weekend = False
    vart = False
    kapott = fuggvenyek.cigar_party(cigars, is_weekend)
    print(
        f"cigaretta szama: {cigars}\n"
        f"hetvege e: {is_weekend} \n"
        f"Vart eredemeny: {vart}\n"
        f"kapott: {kapott} \n"
        f"JO_E?: {vart == kapott}\n")

    print("10. testeset")
    cigars = 40
    is_weekend = False
    vart = True
    kapott = fuggvenyek.cigar_party(cigars, is_weekend)
    print(
        f"cigaretta szama: {cigars}\n"
        f"hetvege e: {is_weekend} \n"
        f"Vart eredemeny: {vart}\n"
        f"kapott: {kapott} \n"
        f"JO_E?: {vart == kapott}\n")


    print("11. testeset")
    cigars = 60
    is_weekend = False
    vart = True
    kapott = fuggvenyek.cigar_party(cigars, is_weekend)
    print(
        f"cigaretta szama: {cigars}\n"
        f"hetvege e: {is_weekend} \n"
        f"Vart eredemeny: {vart}\n"
        f"kapott: {kapott} \n"
        f"JO_E?: {vart == kapott}\n")


cigar_party_teszt()


