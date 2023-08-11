# Explanation in line code 40 to 70

```python
 def draw_table(self):
        tb_space_point = (self.table_space, self.table_size - self.table_space)
        cell_space_point = (self.cell_size, self.cell_size * 2)
        r1 = pygame.draw.line(
            screen,
            self.table_color,
            [tb_space_point[0], cell_space_point[0]],
            [tb_space_point[1], cell_space_point[0]],
            8,
        )
        c1 = pygame.draw.line(
            screen,
            self.table_color,
            [cell_space_point[0], tb_space_point[0]],
            [cell_space_point[0], tb_space_point[1]],
            8,
        )
        r2 = pygame.draw.line(
            screen,
            self.table_color,
            [tb_space_point[0], cell_space_point[1]],
            [tb_space_point[1], cell_space_point[1]],
            8,
        )
        c2 = pygame.draw.line(
            screen,
            self.table_color,
            [cell_space_point[1], tb_space_point[0]],
            [cell_space_point[1], tb_space_point[1]],
            8,
        )
```

Ini adalah sebuah fungsi dalam suatu class yang digunakan untuk menggambar tabel pada layar menggunakan library Pygame. Fungsi ini memiliki beberapa baris kode yang menggambar garis-garis untuk membentuk tabel pada layar.

Baris pertama mendefinisikan titik awal dan titik akhir untuk garis horizontal pertama (r1) menggunakan koordinat dari variabel tb_space_point dan cell_space_point.
Baris kedua menggambar garis horizontal pertama (r1) dengan menggunakan fungsi pygame.draw.line(). Parameter pertama adalah objek screen yang merupakan tampilan utama layar. Parameter kedua adalah warna garis yang ditentukan oleh variabel self.table_color. Parameter ketiga dan keempat adalah koordinat titik awal dan akhir untuk garis horizontal. Parameter kelima adalah ketebalan garis yang ditentukan oleh angka 8.
Baris ketiga dan keempat melakukan hal yang sama seperti baris pertama dan kedua, tetapi untuk menggambar garis vertikal pertama (c1).
Baris kelima hingga kedelapan melakukan hal yang sama dengan baris pertama hingga keempat, tetapi untuk menggambar garis-garis kedua (r2 dan c2).

Jadi, fungsi draw_table(self) ini akan menggambar tabel dengan dua baris dan dua kolom pada layar dengan menggunakan garis-garis yang terdefinisi dalam code di atas.

## Explanations 94 to 97

```python
 screen.blit(
    img,
    (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size),
)
```

Penjelasan baris kode tersebut adalah sebagai berikut:

Padais tersebut, ekspresi (x *self.cell_size, y* self.cell_size, self.cell_size, self.cell_size) digunakan sebagai argumen kedua dalam fungsi screen.blit(). Ekspresi tersebut mendefinisikan rektangle tempat gambar akan digambar di layar.

(x *self.cell_size, y* self.cell_size) merupakan titik koordinat kiri atas dari rektangle tersebut, yang mengindikasikan posisi gambar di layar. Koordinat x dan y dipermukaan layar dikalikan dengan ukuran sel tabel.
self.cell_size merupakan lebar dan tinggi dari rektangle tersebut, yang mengindikasikan ukuran gambar.

Jadi tidak ada dua kali penggunaan self.cell_size dalam baris kode tersebut.
