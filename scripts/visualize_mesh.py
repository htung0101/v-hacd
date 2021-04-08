# visualize vhacd mesh with different color
import trimesh #pymeshlab
import click
import tempfile
import os
import ipdb
st=ipdb.set_trace




@click.command()
@click.option('--input', default='default',
              help='input file for the mesh(.obj).')

def main(input):

    folder_with_mtl_file = "/home/htung/Documents/2021/example_meshes/"
    obj_file = input #"/home/htung/Documents/2021/example_meshes/bell_pepper_vhacd.obj"
    num_mtl = 11


    # edit the obj file to add color
    lines = []
    lines.append("mtllib color.mtl\n")

    n_chunk = 0
    with open(obj_file) as f:
        for line in f:
            lines.append(line)
            if line.startswith("o "):
                # add material
                mat_id = n_chunk % num_mtl
                lines.append(f"usemtl mat{mat_id}\n")
                n_chunk += 1


    tmpfile_name = os.path.join(folder_with_mtl_file, "tmp.obj")

    with open(tmpfile_name, 'w') as f:
        f.writelines(lines)


    m = trimesh.load(tmpfile_name)
    m.show()
    os.remove(tmpfile_name)


if __name__ == '__main__':
    main()
