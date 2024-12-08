
with open("data/day5.txt") as file:
    fich = [l.strip() for l in file]

aux = fich.index('')
rules = [x.split("|") for x in fich[:aux]] # --> 0 before 1
#has_rule = [x[1] for x in rules]  # 1s
#condition = [x[0] for x in rules] # 0s

#pages = ",".join(fich[aux+1:]).split(",")
pages = [x.split(",") for x in fich[aux+1:]]



star_1 = 0
remove_indexes = []
for page in pages:
    page_ok = True
    for [before, after] in rules:
        if not page_ok:
            break
        # if both numbers in page and ordered ok
        if before in page and after in page:
            page_ok = page_ok and page.index(before) < page.index(after)
    #print(page, page_ok)
    if page_ok:
        star_1 += int(page[int(len(page)/2)])
        remove_indexes += [pages.index(page)]

print("star 1:", star_1)


#delete correct pages
# and remember that if removed from smallest to largest index, indexes in the list change (:
for x in reversed(remove_indexes):
    del pages[x]

#print("rules:", rules)
#print("pages:", pages)

def my_insert(page, elem, rules):
    #get rules that apply to elem
    rules_before = [[x,y] for [x,y] in rules if x==elem]
    rules_after = [[x,y] for [x,y] in rules if y==elem]
    #get indexes for values where elem has to be before/after
    indexes_before =  [page.index(y) for [_,y] in rules_before if y in page]
    indexes_after = [page.index(x) for [x,_] in rules_after if x in page]
    max_after = max(indexes_after) if len(indexes_after)>0 else -1
    min_before = min(indexes_before) if len(indexes_before)>0 else -1
    #if not in rules, put it at the beginning
    if max_after==-1 and min_before==-1:
        page.insert(0, elem)
        return page
    #if has before but not after,
    if max_after==-1:
        page.insert(min_before, elem)
        return page
    #if has after but not before,
    if min_before==-1:
        page.insert(max_after+1, elem)
        return page
    
    # new index is between biggest after and smallest before
    if max_after < min_before:
        page.insert(max_after+1 , elem)
        return page
    
    print("ERROR. Page not feasible with provided rules")
    return []


star_2=0
for page in pages:
    new_page = []
    new_rules = []
    # get rules that applies to the page
    for [before, after] in rules:
        if before in page and after in page:
            new_rules.append([before, after])
    for elem in page:
        new_page = my_insert(new_page, elem, new_rules)
    #print(page, "->", new_page)
    star_2 += int(new_page[int(len(new_page)/2)])

print("star 2:", star_2)

# time for star 1 -> 19.42 min
# time for star 2 -> 1.12.20 min
# time for day 5 ->  1.22.02min
