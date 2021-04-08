# test the build file
./build/linux/test/testVHACD  --pca 0 --maxBBoxLen 1.0 --alpha 1.5 --beta 0 --randSeed 2 --selectFromTopK 5 --resolution 1000000 --maxVolumePerCH 1 --concavity 0.0001 --mode 0 --input /home/htung/Documents/2021/example_meshes/bell_pepper.obj --output /home/htung/Documents/2021/example_meshes/bell_pepper_vhacd.obj --log

#./build/linux/test/testVHACD --input /home/htung/Documents/2021/example_meshes/Garlic.obj --alpha 0.01  --resolution=1000000 --concavity 0.0001  --output /home/htung/Documents/2021/example_meshes/Garlic_vhacd.obj





# visualize the mesh
python scripts/visualize_mesh.py --input /home/htung/Documents/2021/example_meshes/bell_pepper_vhacd.obj

#python scripts/visualize_mesh.py --input /home/htung/Documents/2021/example_meshes/Garlic_vhacd.obj