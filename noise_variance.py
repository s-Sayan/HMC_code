import numpy as np
import healpy as hp

#Readng the maps

nside=2048
npix=12*nside*nside
noiset=np.ndarray(shape=(200,npix))
noiseq=np.ndarray(shape=(200,npix))
noiseu=np.ndarray(shape=(200,npix))
noisee=np.ndarray(shape=(200,npix))
noiseb=np.ndarray(shape=(200,npix))
noise = np.ndarray(shape=(3,npix))
index=0

for i in range(0,10):
    print(index)
    noiset[index] = hp.ud_grade(hp.read_map("./full_mission_noise/dx12_v3_smica_noise_mc_0000"+str(i)+"_raw.fits", field=0), nside_out=2048)
    noiseq[index] = hp.ud_grade(hp.read_map("./full_mission_noise/dx12_v3_smica_noise_mc_0000"+str(i)+"_raw.fits", field=1), nside_out=2048)
    noiseu[index] = hp.ud_grade(hp.read_map("./full_mission_noise/dx12_v3_smica_noise_mc_0000"+str(i)+"_raw.fits", field=2), nside_out=2048)
    index = index+1


for i in range(10,100):
    print(index)
    noiset[index] = hp.ud_grade(hp.read_map("./full_mission_noise/dx12_v3_smica_noise_mc_000"+str(i)+"_raw.fits", field=0), nside_out=2048)
    noiseq[index] = hp.ud_grade(hp.read_map("./full_mission_noise/dx12_v3_smica_noise_mc_000"+str(i)+"_raw.fits", field=1), nside_out=2048)
    noiseu[index] = hp.ud_grade(hp.read_map("./full_mission_noise/dx12_v3_smica_noise_mc_000"+str(i)+"_raw.fits", field=2), nside_out=2048)
    index = index+1

for i in range(100,200):
    print(index)
    noiset[index] = hp.ud_grade(hp.read_map("./full_mission_noise_from_100/dx12_v3_smica_noise_mc_00"+str(i)+"_raw.fits", field=0), nside_out=2048)
    noiseq[index] = hp.ud_grade(hp.read_map("./full_mission_noise_from_100/dx12_v3_smica_noise_mc_00"+str(i)+"_raw.fits", field=1), nside_out=2048)
    noiseu[index] = hp.ud_grade(hp.read_map("./full_mission_noise_from_100/dx12_v3_smica_noise_mc_00"+str(i)+"_raw.fits", field=2), nside_out=2048)
    index = index+1
print("Reading map is done")
for i in range(0,200):
    noise[0,:] = noiset[i,:]
    noise[1,:] = noiseq[i,:]
    noise[2,:] = noiseu[i,:]
    alms = hp.map2alm(noise,pol=True,lmax=1500)
    noisee[i]= hp.alm2map(alms[1,:],pol=False,lmax=1500,nside=2048) #check if mask needs to be mutilplied here as well
    noiseb[i] = hp.alm2map(alms[2,:],pol=False,lmax=1500,nside=2048)
print('Converted to e and b maps')

noise_vare = np.var(noisee,axis=0)
noise_varb = np.var(noiseb,axis=0)
print("Variance calc is done")
noise_vare = np.var(noisee,axis=0)
np.savetxt("Noise_variance_emap_ffp10_from0to199_nside2048_oncemore.dat", noise_vare)
exit()
