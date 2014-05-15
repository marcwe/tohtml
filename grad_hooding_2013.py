#!/usr/bin/python



f = open('grad_hooding_2013.html', 'w')

myList=['PCO_3557.jpg' , 'PCO_3560.jpg' , 'PCO_3561.jpg' , 'PCO_3562.jpg' , 'PCO_3566.jpg' , 'PCO_3567.jpg' , 'PCO_3568.jpg' , 'PCO_3570.jpg' , 'PCO_3571.jpg' , 'PCO_3572.jpg' , 'PCO_3573.jpg' , 'PCO_3577.jpg' , 'PCO_3578.jpg' , 'PCO_3579.jpg' , 'PCO_3580.jpg' , 'PCO_3582.jpg' , 'PCO_3583.jpg' , 'PCO_3585.jpg' , 'PCO_3588.jpg' , 'PCO_3589.jpg' , 'PCO_3590.jpg' , 'PCO_3592.jpg' , 'PCO_3593.jpg' , 'PCO_3595.jpg' , 'PCO_3596.jpg' , 'PCO_3598.jpg' , 'PCO_3599.jpg' , 'PCO_3600.jpg' , 'PCO_3603.jpg' , 'PCO_3604.jpg' , 'PCO_3605.jpg' , 'PCO_3606.jpg' , 'PCO_3607.jpg' , 'PCO_3608.jpg' , 'PCO_3609.jpg' , 'PCO_3611.jpg' , 'PCO_3613.jpg' , 'PCO_3614.jpg' , 'PCO_3615.jpg' , 'PCO_3617.jpg' , 'PCO_3618.jpg' , 'PCO_3619.jpg' , 'PCO_3620.jpg' , 'PCO_3621.jpg' , 'PCO_3622.jpg' , 'PCO_3624.jpg' , 'PCO_3625.jpg' , 'PCO_3626.jpg' , 'PCO_3627.jpg' , 'PCO_3628.jpg' , 'PCO_3629.jpg' , 'PCO_3630.jpg' , 'PCO_3631.jpg' , 'PCO_3632.jpg' , 'PCO_3633.jpg' , 'PCO_3635.jpg' , 'PCO_3636.jpg' , 'PCO_3637.jpg' , 'PCO_3638.jpg' , 'PCO_3640.jpg' , 'PCO_3641.jpg' , 'PCO_3643.jpg' , 'PCO_3644.jpg' , 'PCO_3646.jpg' , 'PCO_3647.jpg' , 'PCO_3648.jpg' , 'PCO_3649.jpg' , 'PCO_3650.jpg' , 'PCO_3651.jpg' , 'PCO_3652.jpg' , 'PCO_3653.jpg' , 'PCO_3654.jpg' , 'PCO_3655.jpg' , 'PCO_3656.jpg' , 'PCO_3657.jpg' , 'PCO_3658.jpg' , 'PCO_3659.jpg' , 'PCO_3660.jpg' , 'PCO_3661.jpg' , 'PCO_3662.jpg' , 'PCO_3663.jpg' , 'PCO_3664.jpg' , 'PCO_3665.jpg' , 'PCO_3666.jpg' , 'PCO_3668.jpg' , 'PCO_3669.jpg' , 'PCO_3670.jpg' , 'PCO_3671.jpg' , 'PCO_3673.jpg' , 'PCO_3674.jpg' , 'PCO_3675.jpg' , 'PCO_3676.jpg' , 'PCO_3677.jpg' , 'PCO_3679.jpg' , 'PCO_3682.jpg' , 'PCO_3684.jpg' , 'PCO_3685.jpg' , 'PCO_3686.jpg' , 'PCO_3687.jpg' , 'PCO_3688.jpg' , 'PCO_3689.jpg' , 'PCO_3690.jpg' , 'PCO_3692.jpg' , 'PCO_3693.jpg' , 'PCO_3694.jpg' , 'PCO_3696.jpg' , 'PCO_3697.jpg' , 'PCO_3698.jpg' , 'PCO_3699.jpg' , 'PCO_3700.jpg' , 'PCO_3701.jpg' , 'PCO_3702.jpg' , 'PCO_3703.jpg' , 'PCO_3705.jpg' , 'PCO_3707.jpg' , 'PCO_3708.jpg' , 'PCO_3709.jpg' , 'PCO_3710.jpg' , 'PCO_3711.jpg' , 'PCO_3712.jpg' , 'PCO_3713.jpg' , 'PCO_3714.jpg' , 'PCO_3716.jpg' , 'PCO_3717.jpg' , 'PCO_3718.jpg' , 'PCO_3719.jpg' , 'PCO_3720.jpg' , 'PCO_3721.jpg' , 'PCO_3722.jpg' , 'PCO_3723.jpg' , 'PCO_3724.jpg' , 'PCO_3725.jpg' , 'PCO_3726.jpg' , 'PCO_3728.jpg' , 'PCO_3729.jpg' , 'PCO_3730.jpg' , 'PCO_3731.jpg' , 'PCO_3732.jpg' , 'PCO_3733.jpg' , 'PCO_3734.jpg' , 'PCO_3735.jpg' , 'PCO_3736.jpg' , 'PCO_3737.jpg' , 'PCO_3739.jpg' , 'PCO_3740.jpg' , 'PCO_3741.jpg' , 'PCO_3742.jpg' , 'PCO_3743.jpg' , 'PCO_3744.jpg' , 'PCO_3745.jpg' , 'PCO_3746.jpg' , 'PCO_3747.jpg' , 'PCO_3748.jpg' , 'PCO_3749.jpg' , 'PCO_3750.jpg' , 'PCO_3751.jpg' , 'PCO_3752.jpg' , 'PCO_3753.jpg' , 'PCO_3754.jpg' , 'PCO_3755.jpg' , 'PCO_3756.jpg' , 'PCO_3757.jpg' , 'PCO_3758.jpg' , 'PCO_3759.jpg' , 'PCO_3760.jpg' , 'PCO_3761.jpg' , 'PCO_3762.jpg' , 'PCO_3763.jpg' , 'PCO_3764.jpg' , 'PCO_3765.jpg' , 'PCO_3766.jpg' , 'PCO_3767.jpg' , 'PCO_3768.jpg' , 'PCO_3769.jpg' , 'PCO_3770.jpg' , 'PCO_3771.jpg' , 'PCO_3772.jpg' , 'PCO_3773.jpg' , 'PCO_3774.jpg' , 'PCO_3775.jpg' , 'PCO_3776.jpg' , 'PCO_3777.jpg' , 'PCO_3778.jpg' , 'PCO_3779.jpg' , 'PCO_3780.jpg' , 'PCO_3781.jpg' , 'PCO_3782.jpg' , 'PCO_3783.jpg' , 'PCO_3784.jpg' , 'PCO_3785.jpg' , 'PCO_3786.jpg' , 'PCO_3787.jpg' , 'PCO_3788.jpg' , 'PCO_3789.jpg' , 'PCO_3791.jpg' , 'PCO_3792.jpg' , 'PCO_3793.jpg' , 'PCO_3794.jpg' , 'PCO_3795.jpg' , 'PCO_3796.jpg' , 'PCO_3797.jpg' , 'PCO_3798.jpg' , 'PCO_3799.jpg']

f.write ('<html><head><title>Graduate Commencement Hoodings 2013</title></head><body><table><tr>')

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
 
	if (i+1)%5==0: f.write ('</tr><tr>\n')
	i = i + 1
	
f.write ('</tr></table></body></html>')	
	
f.closed