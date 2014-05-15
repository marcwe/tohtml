#!/usr/bin/python



f = open('grad_commenc_2013.html', 'w')

myList=['PCO_3180.jpg' , 'PCO_3182.jpg' , 'PCO_3188.jpg' , 'PCO_3190.jpg' , 'PCO_3191.jpg' , 'PCO_3194.jpg' , 'PCO_3199.jpg' , 'PCO_3202.jpg' , 'PCO_3204.jpg' , 'PCO_3208.jpg' , 'PCO_3210.jpg' , 'PCO_3211.jpg' , 'PCO_3213.jpg' , 'PCO_3220.jpg' , 'PCO_3224.jpg' , 'PCO_3229.jpg' , 'PCO_3234.jpg' , 'PCO_3235.jpg' , 'PCO_3237.jpg' , 'PCO_3240.jpg' , 'PCO_3241.jpg' , 'PCO_3244.jpg' , 'PCO_3245.jpg' , 'PCO_3248.jpg' , 'PCO_3250.jpg' , 'PCO_3260.jpg' , 'PCO_3264.jpg' , 'PCO_3265.jpg' , 'PCO_3267.jpg' , 'PCO_3270.jpg' , 'PCO_3271.jpg' , 'PCO_3276.jpg' , 'PCO_3278.jpg' , 'PCO_3280.jpg' , 'PCO_3281.jpg' , 'PCO_3283.jpg' , 'PCO_3284.jpg' , 'PCO_3289.jpg' , 'PCO_3291.jpg' , 'PCO_3292.jpg' , 'PCO_3297.jpg' , 'PCO_3298.jpg' , 'PCO_3299.jpg' , 'PCO_3305.jpg' , 'PCO_3307.jpg' , 'PCO_3323.jpg' , 'PCO_3331.jpg' , 'PCO_3337.jpg' , 'PCO_3338.jpg' , 'PCO_3346.jpg' , 'PCO_3351.jpg' , 'PCO_3356.jpg' , 'PCO_3359.jpg' , 'PCO_3363.jpg' , 'PCO_3366.jpg' , 'PCO_3369.jpg' , 'PCO_3371.jpg' , 'PCO_3373.jpg' , 'PCO_3378.jpg' , 'PCO_3393.jpg' , 'PCO_3395.jpg' , 'PCO_3397.jpg' , 'PCO_3399.jpg' , 'PCO_3400.jpg' , 'PCO_3401.jpg' , 'PCO_3402.jpg' , 'PCO_3406.jpg' , 'PCO_3409.jpg' , 'PCO_3411.jpg' , 'PCO_3419.jpg' , 'PCO_3422.jpg' , 'PCO_3426.jpg' , 'PCO_3431.jpg' , 'PCO_3435.jpg' , 'PCO_3438.jpg' , 'PCO_3448.jpg' , 'PCO_3449.jpg' , 'PCO_3452.jpg' , 'PCO_3456.jpg' , 'PCO_3463.jpg' , 'PCO_3465.jpg' , 'PCO_3467.jpg' , 'PCO_3468.jpg' , 'PCO_3473.jpg' , 'PCO_3476.jpg' , 'PCO_3485.jpg' , 'PCO_3490.jpg' , 'PCO_3495.jpg' , 'PCO_3500.jpg' , 'PCO_3504.jpg' , 'PCO_3511.jpg' , 'PCO_3518.jpg' , 'PCO_3531.jpg' , 'PCO_3534.jpg' , 'PCO_3545.jpg' , 'PCO_3552.jpg' , 'PCO_3553.jpg' , 'PCO_3564.jpg' , 'PCO_3576.jpg' , 'PCO_3597.jpg' , 'PCO_3610.jpg' , 'PCO_3616.jpg' , 'PCO_3642.jpg' , 'PCO_3681.jpg' , 'PCO_3738.jpg' , 'PCO_3790.jpg' , 'PCO_3801.jpg' , 'PCO_3811.jpg' , 'PCO_3814.jpg' , 'PCO_3815.jpg' , 'PCO_3816.jpg' , 'PCO_3817.jpg' , 'PCO_3818.jpg' , 'PCO_3820.jpg' , 'PCO_3821.jpg' , 'PCO_3823.jpg' , 'PCO_3824.jpg' , 'PCO_3827.jpg'
]

f.write ('<html><head><title>Graduate Commencement 2013</title></head><body><table><tr>')

i = 0
while i < len(myList):

	print myList[i]

	fil = myList[i]

	f.write ('<td><a href="full/')
	f.write (fil)
	f.write ('"><img src="')
	f.write (fil)
	f.write ('" alt="')
	f.write (fil)
	f.write ('" /></a></td>')
	f.write ('\n')
 
	if (i+1)%3==0: f.write ('</tr><tr>\n')
	i = i + 1
	
f.write ('</tr></table></body></html>')	
	
f.closed