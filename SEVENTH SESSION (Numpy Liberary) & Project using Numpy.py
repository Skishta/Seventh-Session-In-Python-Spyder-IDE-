'''بسم الله الرحمن الرحيم'''               

                     #SEVENTH SESSION (Numpy Liberary) & Project using Numpy
#ال numpy هي مكتبة يتم استخدامها فى البايثون
#وهى مكتبة يتم استعمالها لانها تحتوى على mathimatics functions
import numpy as np
#يتم تسميتها باختصار فقط للتسهيل
#سوف نسستخدم ال array function
#to store array in numpy in variable
 C=np.array([1,2,3,5])
#to change type of array
a=np.array([1,2,3,5],dtype=np.float64)
#to print the variable assigned
print(a)
#لطباعة array بها اكثر من عنصر 
B=np.array([[20,30,40,25],[60,70,90,99],[10,50,100,55]],dtype=np.float64)
#لطباعة عنصر محدد من داخل ال array
#مثلا عايز اطبع الصف الثانى  بالكامل (second raw) من المصفوفة
print(a[2])
#اذا كان ال array مكون من اكثر من rows & columns وتحتاج لطباعة عنصر معين
#طيب لو عايز اطبع رقم معين من الصف الثانى
#مثلا عايز اطبع رقم (90) من الصف الثانى 
#يتم تسمية العنصر الكبير ثم العنصر الصغير وهكذا
#to print number 90 [index(2)] in the second raw
print(B[1][2])
#OR
print(B[1,2])
#لطباعة نوع ال array لليوزر العادى 
type(a)
type(B)
#لطباعة array مكونة من أصفار..يتم تحديد عدد ال rows,columns داخل اقواس function
#example for 'zeros' array (3*3) 
zer=np.zeros((3,3))
#لطباعة array مكونة من "واحد"..يتم تحديد عدد ال rows,columns داخل اقواس function
#example for 'ones' array (3*3) 
ones=np.ones((3,3))
#لطباعة array مكونة من رقم معين
#يتم تحديد حجم ال array ثم كتابة الرقم المراد إدخالة
fourth=np.full((3,3),4)
#لعمل one dimesional array "مصفوفة ال واحد
#بمعنى ان يكون معاك رقم "واحد" على القطر الرئيسي فقط
unity=np.eye(3)
#إذا اردت ان تسحب ارقام معينة من array معينة وتعملها assign فى متغير اخر مثلا
G=a[1:4]
#افرض انت عندك array مكونة من اكثر من اعمدة وصفوف
#وتريد طباعة أعمدة وصفوف معينة بالمصفوفة
#مثلا انا عايز اطبع من اول الصف الثانى حتى الصف الاخير
#وفى الاعمدة عايز اطبع من اول العمود الاول حتى العمود الثانى
#slice specific raws & columns from the array
#for example [D=b[الرقم التالي للاعمدة, الرقم التالي للصف , بداية الصف ]]
D=B[2:4,1:3]
#to know the type of the new matrix (D)
D.dtype
#لعمل عمليات حسابية على الarray ولكن لابد من تحقق الشرط وهو عدد العناصر متساوية فى الاتنين
print(a+C)
print(a*C)
#لجمع رقم معين على الarray
print(a+10)
#لضرب arrays فى بعض بطريقة ضرب ال matrix
print(np.dot(a,B))
#لايستطيع الضرب لانها لاتجوز.ولابد من تغيير شكل الarray
#لتغيير شكل الarray 
N=B.reshape(1,12)