import csv
def fun1():
    with open("lab_11_data.csv", "r") as source:
        reader = csv.reader(source)
        
        with open("output.csv", "w") as result:
            writer = csv.writer(result)
            for r in reader:
                mp=[]
                for i in range(len(r)-6):
                    mp.append(r[i])
                x=tuple(mp)
                writer.writerow(x)
                mpx.append(mp)

def fun2():
	global mpx
	mpx = list(filter(lambda x: float(x[6]) > -3.0, mpx[1:]))
	for i in mpx:
		print(i)
	print(n)
def fun3():
    global mpx
    n=len(mpx)
    avg1=0
    avg2=0
    avg3=0
    avg1 = sum(list(map(lambda x: float(x[1].replace(",", ""))/n, mpx)))
    avg2 = sum(list(map(lambda x: float(x[2].replace(",", ""))/n, mpx)))
    avg3 = sum(list(map(lambda x: float(x[3].replace(",", ""))/n, mpx)))
    avg=[str(avg1),str(avg2),str(avg3)]
    with open("avg_output.txt","w") as fi:
        fi.write("\n".join(avg))
    print(avg1,avg2,avg3)


mpx=[]
n=len(mpx)

fun1()
n=len(mpx)
fun2()
n=len(mpx)
fun3()
n=len(mpx)
# fun4()
# n=len(mpx)
# fun5()


