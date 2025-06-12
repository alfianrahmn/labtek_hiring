# main.py – Task 1: Earliest Discount
# ------------------------------------------------------------
# 1) Definisi data (bisa diganti atau input manual)
prices_list = [3, 4, 1, 2, 1]  # contoh list harga nanti override by input user

# ------------------------------------------------------------
# 2) Main function : cari index pertama di mana terjadi diskon
def earliest_discount_list(prices):
    """
    Menerima list of int 'prices'.
    Kembalikan index pertama i di mana:
      prices[i] < prices[i-1]  AND  prices[i] < prices[0]
    Jika tidak ada, kembalikan 0.
    """
    if len(prices) < 2:
        return 0  # empty list atau hanya 1 element

    first = prices[0]  # harga pertama
    for i in range(1, len(prices)):
        if prices[i] < prices[i - 1] and prices[i] < first:
            return i
    return 0

# ------------------------------------------------------------
# 2b) BONUS function: tahan gangguan noise singkat
def earliest_discount_robust(prices, window=3):
    """
    Seperti earliest_discount_list(), tapi cek sliding window
    sehingga drop singkat (noise) diabaikan.
    (logic window saya refer dari ChatGPT)
    """
    n = len(prices)
    if n < 2:
        return 0

    first = prices[0]
    for i in range(1, n):
        # cek kandidat diskon
        if not (prices[i] < prices[i - 1] and prices[i] < first):
            continue
        # tentukan window
        left = max(0, i - window // 2)
        right = min(n, i + window // 2 + 1)
        # validasi sustained drop
        if all(prices[i] <= prices[j] for j in range(left, right)):
            return i
    return 0

# ------------------------------------------------------------
# 3) Helper: menerima string (spasi‐delimited) lalu panggil fungsi
def earliest_discount_str(prices_str):
    # parsing split+int() saya cek di Google
    parts = prices_str.split()
    nums = [int(p) for p in parts]
    return earliest_discount_list(nums)

# ------------------------------------------------------------
# 4) Demo / entry‐point
if __name__ == "__main__":
    print("=== Task 1: Earliest Discount ===")
    # Versi 1: standar
    idx1 = earliest_discount_list(prices_list)
    print(f"> Dari list      : {prices_list} → index = {idx1}")

    # Versi 2: robust (bonus)
    idx1r = earliest_discount_robust(prices_list)
    print(f"> Dari list [robust] : {prices_list} → index = {idx1r}")

    # Versi 3: pakai input user (string)
    s = input("Masukkan harga (dipisah spasi), ENTER kosong untuk skip: ").strip()
    if s:
        idx2 = earliest_discount_str(s)
        print(f"> Dari string standard: '{s}' → index = {idx2}")
        nums = [int(x) for x in s.split()]
        idx2r = earliest_discount_robust(nums)
        print(f"> Dari string [robust]: '{s}' → index = {idx2r}")
