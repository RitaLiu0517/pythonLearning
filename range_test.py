# range 範圍 清單產生器

import random

range(5) #[0,1,2,3,4]
range(3) #[0,1,2]

range(2, 5) #[2,3,4]
range(8, 10) #[8,9]
range(2, 10, 3) #[2,5,7] 遞增3
range(3, 8, 2) #[3,5,7] 遞增2
range(10, 3, -2)#[10,8,6,4] 遞減2


for i in range(5) :
    r = random.randint(1,1000)
    print(r)

