test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
#paint_calc(height=test_h, width=test_w, cover=coverage)
area = test_h*test_w
paint_req = round(area/coverage)
print(f"number of can required is{paint_req}")