# Task 1 – Earliest Discount + Bonus Challenge

## Ringkasan Solusi Dasar

Fungsi utama bernama `earliest_discount_list(prices)` menerima list harga (List[int]) dan mencari **index pertama** di mana harga `i`:
- lebih murah dari harga sebelumnya (`i-1`)
- dan juga lebih murah dari harga pertama (`prices[0]`)

Jika kondisi ini tidak ditemukan, fungsi akan mengembalikan `0`.

```python_code```
# contoh
prices = [3, 4, 1, 2]
# → return 2, karena 1 < 4 dan 1 < 3


## Ringkasan Solusi Versi Bonus – Penyesuaian untuk Noise Sementara
Kadang, ada harga yang turun sesaat (spike turun cepat lalu naik lagi), dan itu bukan sinyal diskon nyata.

Fungsi tambahan earliest_discount_robust(prices, window=3) mengecek apakah harga yang turun benar-benar berlangsung stabil dalam window kecil (default 3). Artinya, harga pada index tersebut harus tetap lebih rendah dari tetangganya di sekitar.

# cari harga[i] yang lebih rendah dari sebelumnya dan dari harga awal
# lalu cek apakah harga[i] <= harga[j] untuk semua j di sekitar i (±1)

```python_code```
# contoh
prices = [10, 15, 8, 16, 14]
# → robust return 2 jika 8 tetap lebih kecil dari kiri/kanan
