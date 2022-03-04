print("Welcome! First, I need some information from you.")
fname = lower(input("Please enter your first name: "))
mname = lower(input("Please enter your middle name (leave blank if you don't have one): "))
lname = lower(input("Please enter your last name: "))
mdate = input("Please enter your birth month (MM): ")
ddate = input("Please enter your birth day (DD): ")
ydate = input("Please enter your birth year (YYYY): ")

f_name = ''.join(filter(str.isalpha,fname))
m_name = ''.join(filter(str.isalpha,mname))
l_name = ''.join(filter(str.isalpha,lname))

while True:
    if str.isnumeric(mdate) is False:
        print("Error: Please enter a number for your birth month.")
        mdate = input("Birth month (MM): ")
    if str.isnumeric(ddate) is False:
        print("Error: Please enter a number for your birth day.")
        ddate = input("Birth day (DD): ")
    if str.isnumeric(ydate) is False:
        print("Error: Please enter a number for your birth year.")
        ydate = input("Birth year (YYYY): ")

birth = input("Is the name you entered your birth name? (Y/N): ")

if birth == "N":
    fbname = lower(input("Please enter your first name: "))
    mbname = lower(input("Please enter your middle name (leave blank if you don't have one): "))
    lbname = lower(input("Please enter your last name: "))
    fb_name = ''.join(filter(str.isalpha,fbname))
    mb_name = ''.join(filter(str.isalpha,mbname))
    lb_name = ''.join(filter(str.isalpha,lbname))
else:
    fbname = f_name
    mbname = m_name
    lbname = l_name
if birth == "Y":
    birth = input("Has your name changed? (Y/N): ")
    if birth == "Y":
        fnname = lower(input("Please enter your first name: "))
        mnname = lower(input("Please enter your middle name (leave blank if you don't have one): "))
        lnname = lower(input("Please enter your last name: "))
        fn_name = ''.join(filter(str.isalpha,fnname))
        mn_name = ''.join(filter(str.isalpha,mnname))
        ln_name = ''.join(filter(str.isalpha,lnname))
    else:
        pass

compdate = ''.join(ddate,mdate,ydate)
compname = ''.join(f_name,m_name,l_name)

def lifepath(month,day,year):
    lifepathm = 0
    lifepathd = 0
    lifepathy = 0
    x = 0
    for i in range(0,len(month)):
        lifepathm += i
        while lifepathm > 9 and lifepathm != 11 and lifepathm != 22 and lifepathm != 33:
            for i in range(0,len(lifepathm)):
                x += i
                lifepathm = x
            x = 0
        return lifepathm
    for i in range(0,len(day)):
        lifepathd += i
        while lifepathd > 9 and lifepathd != 11 and lifepathd != 22 and lifepathd != 33:
            for i in range(0,len(lifepathd)):
                x += i
                lifepathd = x
            x = 0
        return lifepathd
    for i in range(0,len(year)):
        lifepathy += i
        while lifepathy > 9 and lifepathy != 11 and lifepathy != 22 and lifepathy != 33:
            for i in range(0,len(lifepathy)):
                x += i
                lifepathy = x
            x = 0
        return lifepathy
    lifepath = lifepathd + lifepathm + lifepathy
    while lifepath > 9 and lifepath != 11 and lifepath != 22:
        for i in range(0,len(lifepath)):
            x += i
        lifepath = x
        x = 0
    return lifepath

def destinynumber(first, mid, last):
    x = 0
    for i in range(0,len(first)):
        sumf = 0
        if i == "a" or i == "j" or i == "s":
            sumf += 1
        if i == "b" or i == "k" or i == "t":
            sumf += 2
        if i == "c" or i == "l" or i == "u":
            sumf += 3
        if i == "d" or i == "m" or i == "v":
            sumf += 4
        if i == "e" or i == "n" or i == "w":
            sumf += 5
        if i == "f" or i == "o" or i == "x":
            sumf += 6
        if i == "g" or i == "p" or i == "y":
            sumf += 7
        if i == "h" or i == "q" or i == "z":
            sumf += 8
        if i == "i" or i == "r":
            sumf += 9
        while sumf > 9 and sumf != 11 and sumf != 22 and sumf != 33:
            for i in range(0,len(sumf)):
                x += i
            sumf = x
            x = 0
    for i in range(0,len(mid)):
        summ = 0
        if i == "a" or i == "j" or i == "s":
            summ += 1
        if i == "b" or i == "k" or i == "t":
            summ += 2
        if i == "c" or i == "l" or i == "u":
            summ += 3
        if i == "d" or i == "m" or i == "v":
            summ += 4
        if i == "e" or i == "n" or i == "w":
            summ += 5
        if i == "f" or i == "o" or i == "x":
            summ += 6
        if i == "g" or i == "p" or i == "y":
            summ += 7
        if i == "h" or i == "q" or i == "z":
            summ += 8
        if i == "i" or i == "r":
            summ += 9
        while summ > 9 and summ != 11 and summ != 22 and summ != 33:
            for i in range(0,len(summ)):
                x += i
            summ = x
            x = 0
    for i in range(0,len(last)):
        suml = 0
        if i == "a" or i == "j" or i == "s":
            suml += 1
        if i == "b" or i == "k" or i == "t":
            suml += 2
        if i == "c" or i == "l" or i == "u":
            suml += 3
        if i == "d" or i == "m" or i == "v":
            suml += 4
        if i == "e" or i == "n" or i == "w":
            suml += 5
        if i == "f" or i == "o" or i == "x":
            suml += 6
        if i == "g" or i == "p" or i == "y":
            suml += 7
        if i == "h" or i == "q" or i == "z":
            suml += 8
        if i == "i" or i == "r":
            suml += 9
        while suml > 9 and suml != 11 and suml != 22 and suml != 33:
            for i in range(0,len(suml)):
                x += i
            suml = x
            x = 0
    destiny = sumf + summ + suml
    while destiny > 9 and destiny != 11 and destiny != 22:
        for i in range(0,len(destiny)):
            x += i
        destiny = x
        x = 0
    return destiny

def personalitynum(first,mid,last):
    x = 0
    vowl = ["a","e","i","o","u"]
    if "y" in first:
        z = re.findall(".{0,1}y.{0,1}",first)
        for i in vowl:
            if i in z or z.index("y") == 0:
                sumf += 7
            else:
                sumf += 0
    if "y" in mid:
        z = re.findall(".{0,1}y.{0,1}",mid)
        for i in vowl:
            if i in z or z.index("y") == 0:
                summ += 7
            else:
                summ += 0
    if "y" in last:
        z = re.findall(".{0,1}y.{0,1}",last)
        for i in vowl:
            if i in z or z.index("y") == 0:
                suml += 7
            else:
                suml += 0
    for i in range(0,len(first)):
        sumf = 0
        if i == "j" or i == "s":
            sumf += 1
        if i == "b" or i == "k" or i == "t":
            sumf += 2
        if i == "c" or i == "l":
            sumf += 3
        if i == "d" or i == "m" or i == "v":
            sumf += 4
        if i == "n" or i == "w":
            sumf += 5
        if i == "f" or i == "x":
            sumf += 6
        if i == "g" or i == "p":
            sumf += 7
        if i == "h" or i == "q" or i == "z":
            sumf += 8
        if i == "r":
            sumf += 9
        else:
            sumf += 0
        while sumf > 9 and sumf != 11 and sumf != 22 and sumf != 33:
            for i in range(0,len(sumf)):
                x += i
            sumf = x
            x = 0
    for i in range(0,len(mid)):
        summ = 0
        if i == "j" or i == "s":
            summ += 1
        if i == "b" or i == "k" or i == "t":
            summ += 2
        if i == "c" or i == "l":
            summ += 3
        if i == "d" or i == "m" or i == "v":
            summ += 4
        if i == "n" or i == "w":
            summ += 5
        if i == "f" or i == "x":
            summ += 6
        if i == "g" or i == "p":
            summ += 7
        if i == "h" or i == "q" or i == "z":
            summ += 8
        if i == "r":
            summ += 9
        else:
            summ += 0
        while summ > 9 and summ != 11 and summ != 22 and summ != 33:
            for i in range(0,len(summ)):
                x += i
            summ = x
            x = 0
    for i in range(0,len(last)):
        suml = 0
        if i == "j" or i == "s":
            suml += 1
        if i == "b" or i == "k" or i == "t":
            suml += 2
        if i == "c" or i == "l":
            suml += 3
        if i == "d" or i == "m" or i == "v":
            suml += 4
        if i == "n" or i == "w":
            suml += 5
        if i == "f" or i == "x":
            suml += 6
        if i == "g" or i == "p":
            suml += 7
        if i == "h" or i == "q" or i == "z":
            suml += 8
        if i == "r":
            suml += 9
        else:
            suml += 0
        while suml > 9 and suml != 11 and suml != 22 and suml != 33:
            for i in range(0,len(suml)):
                x += i
            suml = x
            x = 0
    personality = sumf + summ + suml
    while personality > 9 and personality != 11 and personality != 22:
        for i in range(0,len(personality)):
            x += i
        personality = x
        x = 0
    return personality

def soulurgenum(first,mid,last):
    x = 0
    vowl = ["a","e","i","o","u"]
    if "y" in first:
        z = re.findall(".{0,1}y.{0,1}",first)
        for i in vowl:
            if i in z or z.index("y") == 0:
                sumf += 0
            else:
                sumf += 7
    if "y" in mid:
        z = re.findall(".{0,1}y.{0,1}",mid)
        for i in vowl:
            if i in z or z.index("y") == 0:
                summ += 0
            else:
                summ += 7
    if "y" in last:
        z = re.findall(".{0,1}y.{0,1}",last)
        for i in vowl:
            if i in z or z.index("y") == 0:
                suml += 0
            else:
                suml += 7
    for i in range(0,len(first)):
        sumf = 0
        if i == "a":
            sumf += 1
        if i == "u":
            sumf += 3
        if i == "e":
            sumf += 5
        if i == "o":
            sumf += 6
        if i == "i":
            sumf += 9
        else:
            sumf += 0
        while sumf > 9 and sumf != 11 and sumf != 22 and sumf != 33:
            for i in range(0,len(sumf)):
                x += i
            sumf = x
            x = 0
    for i in range(0,len(mid)):
        summ = 0
        if i == "a":
            summ += 1
        if i == "u":
            summ += 3
        if i == "e":
            summ += 5
        if i == "o":
            summ += 6
        if i == "i":
            summ += 9
        else:
            summ += 0
        while summ > 9 and summ != 11 and summ != 22 and summ != 33:
            for i in range(0,len(summ)):
                x += i
            summ = x
            x = 0
    for i in range(0,len(last)):
        suml = 0
        if i == "a":
            suml += 1
        if i == "u":
            suml += 3
        if i == "e":
            suml += 5
        if i == "o":
            suml += 6
        if i == "i":
            suml += 9
        else:
            suml += 0
        while suml > 9 and suml != 11 and suml != 22 and suml != 33:
            for i in range(0,len(suml)):
                x += i
            suml = x
            x = 0
    soulurge = sumf + summ + suml
    while soulurge > 9 and soulurge != 11 and soulurge != 22:
        for i in range(0,len(soulurge)):
            x += i
        soulurge = x
        x = 0
    return soulurge

print("Before we continue, let's define a few terms.")
print("A Life Path number offers insight into your lifetime mission, strengths and weaknesses, and challenges. It alludes to your greater overall purpose.")
print("A Destiny (or Expression) number can describe your traits, character, and destiny. It describes how you will follow your life path.")
print("A Personality number shows what you send out into the world, or how other people perceive you.")
print("A Soul Urge (or Heart's Desire) number represents what your heart and soul crave more than anything else. This is the lens through which you view the world and the motivation for your decisions. If this number matches your Life Path, you'll find acting with true authenticity much easier.")
print("A master number is 11 or 22 (and sometimes 33), which is handled differently in calculations and is not reduced. They are considered more powerful than other numbers.")

print(f'Okay, {fname}, lets look at your numbers!')
print(f'Your Life Path is {lifepath(mdate,ddate,ydate)}. Your Life Path is based on the date you were born.')

if lifepath(mdate,ddate,ydate) == 1:
    print("This Life Path number is associated with leadership and initiative. It is likely that you have a strong personality and can sometimes be known as bossy. However, you also excel in innovation and bringing groups together.")
if lifepath(mdate,ddate,ydate) == 2:
    print("This Life Path number is known for sensitivity and balance. You likely have strong intuition and a skill for peace and harmony.")
if lifepath(mdate,ddate,ydate) == 3:
    print("This Life Path number is very expressive and tends toward creative pursuits. In fact, failing to find this outlet can result in depression!")
if lifepath(mdate,ddate,ydate) == 4:
    print("This Life Path number is associated with stability and productivity. Though you are practical and hardworking, it is important to avoid becoming rigid.")
if lifepath(mdate,ddate,ydate) == 5:
    print("This Life Path number indicates someone who is adventurous and free-thinking. Although this can present as impatience and restlessness, it is also often manifested as adventurousness.")
if lifepath(mdate,ddate,ydate) == 6:
    print("This Life Path number is that of a caretaker who enjoys making those around them happy. You are supportive and empathetic but when you have a bad day, be careful about projecting that to those around you.")
if lifepath(mdate,ddate,ydate) == 7:
    print("This Life Path number is known for analytical and investigative abilities. You are a problem solver and enjoy solitary time to think.")
if lifepath(mdate,ddate,ydate) == 8:
    print("This Life Path number indicates a 'can do', practical type who may not be particularly romantic but is very dependable and ambitious.")
if lifepath(mdate,ddate,ydate) == 9:
    print("This Life Path number is that of an old soul. You are honest--perhaps to a fault--and look to leave the world better than you found it.")
if lifepath(mdate,ddate,ydate) == 11:
    print("This Life Path number shows that you are charismatic and have good instincts.")
if lifepath(mdate,ddate,ydate) == 22:
    print("This Life Path number indicates a connection with the spiritual world and can use that knowledge in daily life.")

print(f'Your Destiny number is {destinynumber(f_name, m_name, l_name)}.')
if f_name != fb_name or m_name != mb_name or l_name != lb_name:
    print(f'The Destiny number associated with your birth name is {destinynumber(fb_name, mb_name, lb_name)}. You may feel more attachment to this number or the one associated with the name you currently use.')
elif fn_name is not None or mn_name is not None or ln_name is not None:
    print(f'The Destiny number associated with your birth name is {destinynumber(fn_name, mn_name, ln_name)}. You may feel more attachment to this number or the one associated with the name you first entered.')

dn = input("Which name would you like to proceed with? (1 = first name entered/2 = second name entered): ")

if dn == 1:
    destinynum = destinynumber(f_name, m_name, l_name)
if dn == 2:
    if f_name != fb_name or m_name != mb_name or l_name != lb_name:
        destinynum = destinynumber(fb_name, mb_name, lb_name)
    elif fn_name is not None or mn_name is not None or ln_name is not None:
        destinynum = destinynumber(fn_name, mn_name, ln_name)

print(f'Okay, your Destiny number is {destinynum}.')

if destinynum == 1:
    print("Your Destiny number indicates that you are a natural leader.")
if destinynum == 2:
    print("Your Destiny number indicates that you are a born diplomat.")
if destinynum == 3:
    print("Your Destiny number indicates that you are an incredible companion.")
if destinynum == 4:
    print("Your Destiny number indicates that you are driven to get things done.")
if destinynum == 5:
    print("Your Destiny number indicates that you are an excellent communicator.")
if destinynum == 6:
    print("Your Destiny number indicates that you are a wonderful nurturer.")
if destinynum == 7:
    print("Your Destiny number indicates that you are a wise educator.")
if destinynum == 8:
    print("Your Destiny number indicates that you are a hard worker.")
if destinynum == 9:
    print("Your Destiny number indicates that you are a natural philanthropist.")
if destinynum == 11:
    print("Your Destiny number indicates that you are a born performer.")
if destinynum == 22:
    print("Your Destiny number indicates that you are a magnetic person.")

if dn == 1:
    pn = personalitynum(f_name, m_name, l_name)
    print(f'Your Personality number is {pn}.')
if dn == 2:
    if f_name != fb_name or m_name != mb_name or l_name != lb_name:
        pn = personalitynum(fb_name, mb_name, lb_name)
        print(f'Your Personality number is {pn}.')
    elif fn_name is not None or mn_name is not None or ln_name is not None:
        pn = personalitynum(fn_name, mn_name, ln_name)
        print(f'Your Personality number is {pn}.')

if pn == 1:
    print("Your Personality number indicates that you are confident, loyal, creative, and have strong leadership skills. You may need to work on your ego, overconfidence, stubbornness, and showing compassion.")
if pn == 2:
    print("Your Personality number indicates that you are trustworthy, honest, reliable, and friendly. You may need to work on moodiness and shyness.")
if pn == 3:
    print("Your Personality number indicates that you are opportunistic, intuitive, creative, and a skilled communicator. You may need to work on your manipulative tendencies.")
if pn == 4:
    print("Your Personality number indicates that you are family-oriented, stylish, stable, nurturing, and pragmatic. You may need to work on a tendency to be too serious.")
if pn == 5:
    print("Your Personality number indicates that you are high-spirited, adaptable, and in search of new experiences. You may need to work on your tendency to overburden yourself.")
if pn == 6:
    print("Your Personality number indicates that you are warm, balanced, responsible, and caring. You may need to work on your tendency to worry and spend frivolously.")
if pn == 7:
    print("Your Personality number indicates that you are intelligent, rational, and dignified. You may need to work on being more outgoing and expressive.")
if pn == 8:
    print("Your Personality number indicates that you are successful, intuitive, and controlled. You may need to work on your tendency to show off and dominate other people.")
if pn == 9:
    print("Your Personality number indicates that you are influential, charming, and confident. You may need to work on your aloofness and entitlement.")
if pn == 11:
    print("Your Personality number indicates that you are sensitive, gentle, patient, and passionate. You may need to work on your vulnerability.")
if pn == 22:
    print("Your Personality number indicates that you are reliable, consistent, and powerful. You may need to work on your self-doubt.")

if dn == 1:
    su = soulurgenum(f_name, m_name, l_name)
    print(f'Your Soul Urge is {su}.')
if dn == 2:
    if f_name != fb_name or m_name != mb_name or l_name != lb_name:
        su = soulurgenum(fb_name, mb_name, lb_name)
        print(f'Your Soul Urge is {su}.')
    elif fn_name is not None or mn_name is not None or ln_name is not None:
        su = soulurgenum(fn_name, mn_name, ln_name)
        print(f'Your Soul Urge is {su}.')

if su == 1:
    print("Your Soul Urge indicates that you are independent and self-sufficient. You are a leader.")
if su == 2:
    print("Your Soul Urge indicates that you are sensitive and emotional. You want to feel secure and comfortable.")
if su == 3:
    print("Your Soul Urge indicates that you are a born entertainer but you need to learn to express your deeper thoughts and feelings.")
if su == 4:
    print("Your Soul Urge indicates that you are disciplined. You are a rock for any undertaking.")
if su == 5:
    print("Your Soul Urge indicates that you are charismatic and infectiously enthusiastic. You need to face your fears.")
if su == 6:
    print("Your Soul Urge indicates that you likely have a close and loyal friend circle. Don't lose sight of your own wants and needs for the sake of others.")
if su == 7:
    print("Your Soul Urge indicates that you are very independent. You need tangible evidence and personal space.")
if su == 8:
    print("Your Soul Urge indicates that you are motivated by building power and wealth and you are skilled at it. Don't lose sight of the bigger picture.")
if su == 9:
    print("Your Soul Urge indicates that you are deeply concerned with global consciousness and have a broader perspective than most.")
if su == 11:
    print("Your Soul Urge indicates that you are on a unique spiritual journey and have a well-developed sense of morality.")
if su == 22:
    print("Your Soul Urge indicates that you are determined to leave a mark on this world.")
