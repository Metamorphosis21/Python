grade_book = {
 'Susan': [92, 85, 100],
 'Eduardo': [83, 95, 79],
 'Azizi': [91, 89, 82],
 'Pantipa': [97, 91, 92]
}
class_total = 0
class_count = 0
for st,st_mark in grade_book.items():
    st_total = sum(st_mark)
    st_avg = st_total/len(st_mark)
    print(f"{st} secured {st_total} and has average {st_avg:.2f}")
    class_total += st_total
    class_count += len(st_mark)
print(f"Class total is {class_total} and class average is {class_total/class_count:.2f}")