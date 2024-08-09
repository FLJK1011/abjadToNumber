text = input ("Enter text : ")

abjad_dict = {
    'ا': 1, 'ب': 2, 'پ': 80, 'ت': 400, 'ث': 500, 'ج': 3, 'چ': 90, 'ح': 8, 'خ': 600,
    'د': 4, 'ذ': 700, 'ر': 200, 'ز': 7, 'ژ': 900, 'س': 60, 'ش': 300, 'ص': 90, 'ض': 800,
    'ط': 9, 'ظ': 900, 'ع': 70, 'غ': 1000, 'ف': 80, 'ق': 100, 'ک': 20, 'گ': 300,
    'ل': 30, 'م': 40, 'ن': 50, 'و': 6, 'ه': 5, 'ی': 10
}

total_sum = sum(abjad_dict[char] for char in text if char in abjad_dict)