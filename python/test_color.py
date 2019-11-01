gu_bdg = 0.4
gu_rdg = 0.6
gl_bdg = 0.5
gl_rdg = 0.5
uut_bdg = 0.45
uut_rdg = 0.45

gu_offset = [(gu_bdg - gl_bdg), (gu_rdg - gl_rdg)]
uut_calib_bdg = uut_bdg - gu_offset[0]
uut_calib_rdg = uut_rdg - gu_offset[1]
print uut_calib_bdg, uut_calib_rdg
print uut_bdg, uut_rdg
print gl_bdg, gl_rdg

