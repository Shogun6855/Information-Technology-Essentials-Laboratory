while True:
    print('''Password must be at least eight characters long
Must contain at least one uppercase letter
Must contain at least one lowercase letter
must contain at least one numeric digit''')
    pw=input("Enter password:")
    l=False
    uc=False
    lc=False
    nu=False
    if len(pw)>8:
        l=True
    for i in pw:
        if 'A'<=i<='Z':
            uc=True
        if 'a'<=i<='z':
            lc=True
        if '0'<=i<='9':
            nu=True
    if l & uc & lc & nu:
        print("The password is valid")
        break
    else:
        print("Enter a valid password")
