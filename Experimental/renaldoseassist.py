print("Welcome to the UAMS Renal Protocol Dose Assist.")
print("This program is intended to present the most relevant part of UAMS's pharmacy-driven renal dosing protocol based upon the parameters you input. It does not provide individualized dosing recommendations and clinical judgment should always be used in deciding the appropriate dose for a patient.")
druglist = [
	["acyclovir", "Zovirax"],
	["ampicillin", "Omnipen"],
	["ampicillin-sulbactam", "Unasyn"], 
	["apixaban", "Eliquis"], 
	["aztreonam","Azactam"], 
	["cefazolin","Ancef"], 
	["cefepime", "Maxipime"], 
	["ceftazidime", "Fortaz", "Tazicef"], 
	["dabigatran", "Pradaxa"], 
	["daptomycin", "Cubicin"], 
	["enoxaparin","Lovenox"], 
	["ertapenem", "Invanz"],
	["famotidine","Pepcid"],
	["fluconazole", "Diflucan"], 
	["ganciclovir", "Cytovene"], 
	["ketorolac", "Toradol"], 
	["levofloxacin", "Levaquin"], 
	["oseltamivir", "Tamiflu"], 
	["meropenem", "Merrem"], 
	["penicillin G", "Pfizerpen"], 
	["piperacillin-tazobactam", "Zosyn"], 
	["rivaroxaban", "Xarelto"], 
	["vancomycin", "Vancocin"]
	]
drug = str.lower(input("Enter drug name (brand or generic) or type LIST: "))
lower = []
for i in range(len(druglist)):
	for j in range(len(druglist[i])):
		lowered = str.lower(druglist[i][j])
		lower.append(lowered)
if drug == "list":
	print("Here is a list of the drugs included in this protocol: ")
	for i in range(len(druglist)):
		print(f'Generic: {druglist[i][0]:25}   Brand: ', end='')
		for j in range(1,len(druglist[i])):
			print(druglist[i][j],end='  ')
		print()
	drug = input("Enter drug name (brand or generic): ")
if drug not in lower:
	print("Error: Please restart.")
else:
	crcl = float(input("Enter patient's most recent creatinine clearance (mL/min): "))
	dialysis = str.upper(input("Is this a dialysis patient? (Y/N): "))
	if dialysis != "Y" and dialysis != "N":
		dialysis = str.upper(input("Please enter Y or N. Is this a dialysis patient? (Y/N): "))
	if dialysis == "Y":
		dialtype = input("What type of dialysis? (HD/PD/CRRT): ")
	if drug == "acyclovir" or drug == "zovirax":
		if dialysis == "N":
			indication = int(input("Is the indication (1) HZV/HSV encephalitis or (2) HSV?: "))
			if indication != 1 and indication != 2:
				indication = int(input("Please enter a number. Is the indication (1) HZV/HSV encephalitis or (2) HSV?: "))
			if crcl > 50 and indication == 1:
				dose = 10
				interval = 8
			if 25 < crcl < 50 and indication == 1:
				dose = 10
				interval = 12
			if 10 <= crcl <= 25 and indication == 1:
				dose = 10
				interval = 24
			if crcl < 10 and indication == 1:
				dose = 5
				interval = 24
			if crcl > 50 and indication == 2:
				dose = 5
				interval = 8
			if 25 < crcl < 50 and indication == 2:
				dose = 5
				interval = 12
			if 10 <= crcl <= 25 and indication == 2:
				dose = 5
				interval = 24
			if crcl < 10 and indication == 2:
				dose = 2.5
				interval = 24
		if dialysis == "Y":
			if dialtype == "HD":
				dose = 5
				interval = 24
			if dialtype == "PD":
				dose = 2.5
				interval = 24
			if dialtype == "CRRT":
				dose = 10
				interval = 24
		print(f'The recommended dose for this patient is {dose} mg/kg IV every {interval} hours.')
		ans = input("Would you like to calculate your patient's dose? (Y/N): ")
		if ans == "N":
			print("Program end.")
		if ans == "Y":
			weight = float(input("Enter patient weight (kg): "))
			admindose = weight * dose
			rounded = round(admindose/50)*50
			print(f'This patient should receive {rounded} mg IV every {interval} hours.')
	elif drug == "ampicillin" or drug == "omnipen":
		load = None
		dose = None
		interval = None
		if dialysis == "N":
			if crcl > 50:
				dose = "1-2"
				interval = "4-6"
			if 10 <= crcl <= 50:
				dose = "1-2"
				interval = "6-12"
			if crcl < 10:
				dose = "1-2"
				interval = "12-24"
			print(f'The recommended dose for this patient is {dose} g IV every {interval} hours.')
		if dialysis == "Y":
			if dialtype == "HD":
				print("The recommended dose for this patient is 1-2 g IV every 12-24 hours.")
			if dialtype == "PD":
				print("The recommended dose for this patient is 250 mg IV every 12 hours.")
			if dialtype == "CRRT":
				print("The recommended dose for this patient is a loading dose of 2 g IV, followed by 1-2 g every 8-12 hours.")
	elif drug == "ampicillin-sulbactam" or drug == "unasyn":
		load = None
		dose = None
		interval = None
		if dialysis == "N":
			if crcl > 30:
				dose = "1.5-3"
				interval = 6
			if 15 <= crcl <= 30:
				dose = "1.5-3"
				interval = 12
			if crcl < 15:
				dose = "1.5-3"
				interval = 24
			print(f'The recommended dose for this patient is {dose} g IV every {interval} hours.')
		if dialysis == "Y":
			if dialtype == "HD":
				print("The recommended dose for this patient is 1.5-3 g IV every 12-24 hours. This medication should be given after dialysis on dialysis days.")
			if dialtype == "PD":
				print("The recommended dose for this patient is 1.5-3 g IV every 24 hours.")
			if dialtype == "CRRT":
				print("The recommended dose for this patient is a loading dose of 3 g IV, followed by 1.5-3 g every 8-12 hours.")
	elif drug == "apixaban" or drug == "eliquis":
		indication = str.upper(input("Is this to treat non-valvular atrial fibrillation? (Y/N): "))
		if indication != "Y" and indication != "N":
			indication = str.upper(input("Please input Y or N. Is this to treat non-valvular atrial fibrillation? (Y/N): "))
		if indication == "Y":
			age = int(input("Enter patient age: "))
			weight = int(input("Enter patient weight (kg): "))
			creatinine = int(input("Enter most recent serum creatinine (mg/dL): "))
			if age >= 80:
				if weight < 60 or creatinine >= 1.5:
					print("Renal dose adjustment is appropriate for this patient. This patient should receive 2.5 mg twice daily.")
				else:
					print("This patient does not require renal dose adjustment. This patient should receive 5 mg twice daily.")
			if age < 80:
				if weight < 60 and creatinine >= 1.5:
					print("Renal dose adjustment is appropriate for this patient. This patient should receive 2.5 mg twice daily.")
				else:
					print("This patient does not require renal dose adjustment. This patient should receive 5 mg twice daily.")
		if indication == "N":
			indication = input("Is this to treat DVT or PE, not including VTE more than 6 months ago? (Y/N): ")
			if indication == "Y":
				print("To treat recent DVT/PE, the patient should receive 10 mg twice daily for seven days and then 5 mg twice daily. No renal dose adjustment is required.")
			if indication == "N":
				print("For VTE prophylaxis or reduced-intensity treatment after initial 6 month treatment, the patient should receive 2.5 mg twice daily. No renal adjustment is required.")
	elif drug == "aztreonam" or drug == "azactam":
		load = None
		dose = None
		interval = None
		if dialysis == "N":
			indication = int(input("Is the indication (1) Pseudomonas or (2) standard?: "))
			if indication != 1 and indication != 2:
				indication = int(input("Please enter a number. Is the indication (1) Pseudomonas or (2) standard?: "))
			if crcl >= 30 and indication == 1:
				print("The recommended dose for this patient is 2 g IV every 6-8 hours.")
			if 10 <= crcl <= 29 and indication == 1:
				print("The recommended dose for this patient is 1 g IV every 6-8 hours.")
			if crcl < 10 and indication == 1:
				print("The recommended dose for this patient is 500 mg IV every 6-8 hours.")
			if crcl >= 30 and indication == 2:
				print("The recommended dose for this patient is 1-2 g IV every 8-12 hours.")
			if 10 <= crcl <= 29 and indication == 2:
				print("The recommended dose for this patient is 500 mg-1 g IV every 8-12 hours.")
			if crcl < 10 and indication == 2:
				print("The recommended dose for this patient is 250-500 mg IV every 8-12 hours. The dose should be about 25% of the dose given in normal renal function.")
		if dialysis == "Y":
			if dialtype == "HD":
				print("The recommended dose for this patient is 500 mg IV every 12 hours.")
			if dialtype == "PD":
				print("The recommended dose for this patient is 1.5-3 g IV every 24 hours.")
			if dialtype == "CRRT":
				print("The recommended dose for this patient is a loading dose of 3 g IV, followed by 1.5-3 g every 8-12 hours.")
	elif drug == "cefazolin" or drug == "ancef":
		if dialysis == "N":
			if crcl >= 30:
				print("The recommended dose for this patient is 1-2 g IV every 8 hours.")
			if crcl < 30:
				print("The recommended dose for this patient is 500 mg-1 g IV every 12 hours. The dose should be about 50% of the dose given in normal renal function.")
		if dialysis == "Y":
			if dialtype == "HD":
				print("The recommended dose for this patient is 500 mg-1 g IV every 24 hours. This medication should be given after dialysis on dialysis days.")
			if dialtype == "PD":
				print("The recommended dose for this patient is 500 mg IV every 12 hours.")
			if dialtype == "CRRT":
				print("The recommended dose for this patient is a loading dose of 2 g IV, followed by 1-2 g every 12 hours.")
	elif drug == "cefepime" or drug == "maxipime":
		if dialysis == "N":
			if crcl > 50:
				dose = 2
				interval = "8-12"
			if 30 <= crcl <= 50:
				dose = 2
				interval = 12
			if 10 <= crcl <= 29:
				dose = 2
				interval = 24
			if crcl < 10:
				dose = 1
				interval = 24
			print(f'The recommended dose for this patient is {dose} g IV every {interval} hours.')
		if dialysis == "Y":
			if dialtype == "HD":
				print("The recommended dose for this patient is 1 g IV every 24 hours. This medication should be given after dialysis on dialysis days.")
			if dialtype == "PD":
				print("The recommended dose for this patient is 2 g IV every 48 hours.")
			if dialtype == "CRRT":
				print("The recommended dose for this patient is a loading dose of 2 g IV, followed by 1-2 g every 12 hours.")
	elif drug == "ceftazidime" or drug == "fortaz" or drug == "tazicef":
		load = None
		dose = None
		interval = None
		if dialysis == "N":
			if crcl > 50:
				dose = "1-2"
				interval = 8
			if 30 <= crcl <= 50:
				dose = "1-2"
				interval = 12
			if 16 <= crcl <= 29:
				dose = 2
				interval = 24
			if 6 <= crcl <= 15:
				dose = 1
				interval = 24
			if crcl <= 5:
				dose = 1
				interval = 48
			print(f'The recommended dose for this patient is {dose} g IV every {interval} hours.')
		if dialysis == "Y":
			if dialtype == "HD":
				print("The recommended dose for this patient is 1 g IV every 24 hours. This medication should be given after dialysis on dialysis days.")
			if dialtype == "PD":
				print("The recommended dose for this patient is a loading dose of 1 g IV, followed by 500 mg every 24 hours.")
			if dialtype == "CRRT":
				print("The recommended dose for this patient is a loading dose of 2 g IV, followed by 1-2 g every 12 hours.")
	elif drug == "dabigatran" or drug == "pradaxa":
		load = None
		dose = None
		interval = None
		if crcl > 30:
			print("The recommended dose for this patient is 150 mg twice daily.")
		if crcl < 30:
			indication = int(input("Is the indication (1) DVT/PE treatment after 5 days of parenteral anticoagulation or (2) non-valvular atrial fibrillation?: "))
			if indication != 1 and indication != 2:
				indication = int(input("Please enter a number. Is the indication (1) DVT/PE treatment after 5 days of parenteral anticoagulation or (2) non-valvular atrial fibrillation: "))
			if crcl >= 15 and indication == 2:
				print("The recommended dose for this patient is 75 mg twice daily; however, patients with this level of renal impairment were excluded from clinical trials and ACCP recommends avoiding use in this patient population. Consider using apixaban (Eliquis) or warfarin (Coumadin).")
			else: 
				print("This medication is contraindicated in this patient. Apixaban (Eliquis) or warfarin (Coumadin) are preferred agents.")
	elif drug == "daptomycin" or drug == "cubicin":
		load = None
		dose = None
		interval = None
		weight = int(input("Dosing is calculated based on total body weight (TBW). Enter patient weight (kg): "))
		if weight > 120:
			print("If patient weight is over 120 kg, call Antimicrobial Stewardship Pharmacist at 405-4843.")
		if weight <= 120:
			if dialysis == "N":
				if crcl >= 30:
					lodose = 4
					hidose = 8
					interval = 24
				if crcl < 30:
					lodose = 4
					hidose = 6
					interval = 48
			if dialysis == "Y":
				if dialtype == "HD":
					lodose = 4
					hidose = 6
					interval = 48
				if dialtype == "PD":
					lodose = 4
					hidose = 6
					interval = 48
				if dialtype == "CRRT":
					dose = 6
					interval = 24
			print(f'The recommended dose for this patient is {dose} mg/kg IV every {interval} hours.')
			ans = input("Would you like to calculate your patient's dose? (Y/N): ")
			if ans == "N":
				print("Program end.")
			if ans == "Y":
				if dialtype == "CRRT":
					admindose = weight * dose
					rounded = round(admindose/50)*50
					print(f'This patient should receive {rounded} mg IV every 24 hours.')
				else:
					loadmindose = weight * lodose
					hiadmindose = weight * hidose
					loround = round(loadmindose/50)*50
					hiround = round(hiadmindose/50)*50
					print(f'This patient should receive {loround}-{hiround} mg IV every {interval} hours.')
	elif drug == "enoxaparin" or drug == "lovenox":
		load = None
		dose = None
		interval = None
		indication = int(input("Is the indication (1) prophylaxis or (2) treatment?: "))
		if indication != 1 and indication != 2:
			indication = int(input("Please enter a number. Is the indication (1) prophylaxis or (2) treatment?: "))
		if indication == 1:
			if dialysis == "N":
				if crcl >= 30:
					dose = 40
					interval = 24
				if crcl < 30:
					dose = 30
					interval = 24
				print(f'The recommended dose for this patient is {dose} mg subQ every {interval} hours.')
			if dialysis == "Y":
				if dialtype == "HD" or dialtype == "PD":
					print("The recommended dose for this patient is 30 mg subQ every 24 hours. Please note: Though it is not contraindicated, the FDA has not approved this drug for use in this patient population.")
				if dialtype == "CRRT":
					print("Another agent should be considered in this population.")
		if indication == 2:
			if dialysis == "N":
				if crcl >= 30:
					print("The recommended dose for this patient is 1 mg/kg subQ every 12 hours OR 1.5 mg/kg subQ every 24 hours.")
				if crcl < 30:
					print("The recommended dose for this patient is 1 mg/kg subQ every 24 hours.")
					if crcl < 10:
						print("Consider drawing anti-Xa levels to monitor.")
			if dialysis == "Y":
				print("The recommended dose for this patient is 1 mg/kg subQ every 24 hours. Please note: Though it is not contraindicated, the FDA has not approved this drug for use in this patient population. Following anti-Xa levels is recommended.")
			ans = input("Would you like to calculate your patient's dose? (Y/N): ")
			if ans == "N":
				print("Program end.")
			if ans == "Y":
				admindose12 = weight
				admindose24 = weight * 1.5
				rounded12 = round(admindose12/10)*10
				rounded24 = round(admindose24/10)*10
				if crcl >= 30:
					print(f'This patient should receive {rounded12} mg subQ every 12 hours OR {rounded24} mg subQ every 24 hours.')
				else:
					print(f'This patient should receive {rounded12} mg subQ every 24 hours.')
	elif drug == "ertapenem" or drug == "invanz":
		load = None
		dose = None
		interval = None
		if dialysis == "N":
			if crcl >= 30:
				print("The recommended dose for this patient is 1 g IV every 24 hours.")
			if crcl < 30:
				print("The recommended dose for this patient is 500 mg IV every 24 hours.")
		if dialysis == "Y":
			if dialtype == "HD":
				print("The recommended dose for this patient is 500 mg IV every 24 hours. This medication should be given after dialysis on dialysis days.")
			if dialtype == "PD" or dialtype == "CRRT":
				print("The recommended dose for this patient is 500 mg IV every 24 hours.")
	elif drug == "famotidine" or drug == "pepcid":
		load = None
		dose = None
		interval = None
		if crcl > 50:
			print("The recommended dose for this patient is 20 mg every 12 hours.")
		else:
			print("The recommended dose for this patient is 20 mg every 24 hours.")
	elif drug == "fluconazole" or drug == "diflucan":
		load = None
		dose = None
		interval = None
		if dialysis == "N":
			if crcl > 50:
				print("The recommended dose for this patient is 200-800 mg every 24 hours.")
			if crcl <= 50:
				print("The recommended dose for this patient is 100-400 mg every 24 hours. The dose should be about 50% of the dose given in normal renal function.")
		if dialysis == "Y":
			if dialtype == "HD":
				print("The recommended dose for this patient is 100-200 mg every 24 hours. This medication should be given after dialysis on dialysis days.")
			if dialtype == "PD":
				print("The recommended dose for this patient is 100-200 mg every 24 hours.")
			if dialtype == "CRRT":
				print("The recommended dose for this patient is a loading dose of 400-800 mg, followed by 200-400 mg every 24 hours.")
	elif drug == "ganciclovir" or drug == "cytovene":
		load = None
		dose = None
		interval = None
		indication = int(input("Is the indication (1) induction or (2) maintenance?: "))
		if indication != 1 and indication != 2:
			indication = int(input("Please enter a number. Is the indication (1) induction or (2) maintenance?: "))
		if indication == 1:
			if dialysis == "N":
				if crcl >= 10:
					if crcl >= 70:
						dose = 5
						interval = 12
					if 50 <= crcl < 70:
						dose = 2.5
						interval = 12
					if 25 <= crcl < 50:
						dose = 2.5
						interval = 24
					if 10 <= crcl < 25:
						dose = 1.25
						interval = 24
					print(f'The recommended dose for this patient is {dose} mg/kg IV every {interval} hours.')
				if crcl < 10:
					dose = 1.25
					print("The recommended dose for this patient is 1.25 mg/kg IV three times per week.")
			if dialysis == "Y":
				if dialtype == "HD" or dialtype == "PD":
					dose = 1.25
					print("The recommended dose for this patient is 1.25 mg/kg IV three times per week. This medication should be given after dialysis on dialysis days.")
				if dialtype == "CRRT":
					dose = 2.5
					interval = 24
					print(f'The recommended dose for this patient is {dose} mg/kg IV every {interval} hours.')
		if indication == 2:
			if dialysis == "N":
				if crcl >= 10:
					if crcl >= 70:
						dose = 5
						interval = 24
					if 50 <= crcl < 70:
						dose = 2.5
						interval = 24
					if 25 <= crcl < 50:
						dose = 1.25
						interval = 24
					if 10 <= crcl < 25:
						dose = 0.625
						interval = 24
					print(f'The recommended dose for this patient is {dose} mg/kg IV every {interval} hours.')
				if crcl < 10:
					dose = 0.625
					print("The recommended dose for this patient is 1.25 mg/kg IV three times per week.")
			if dialysis == "Y":
				if dialtype == "HD" or dialtype == "PD":
					dose = 0.625
					print("The recommended dose for this patient is 1.25 mg/kg IV three times per week. This medication should be given after dialysis on dialysis days.")
				if dialtype == "CRRT":
					dose = 1.25
					interval = 24
					print(f'The recommended dose for this patient is {dose} mg/kg IV every {interval} hours.')
		ans = input("Would you like to calculate your patient's dose? (Y/N): ")
		if ans == "N":
			print("Program end.")
		if ans == "Y":
			admindose = weight*dose
			rounded = round(admindose)
			if type(interval) == int or type(interval) == float:
				print(f'This patient should receive {rounded} mg IV every {interval} hours.')
			else:
				print(f'This patient should receive {rounded} mg IV three times weekly.')
	elif drug == "ketorolac" or drug == "toradol":
		load = None
		dose = None
		interval = None
		if crcl < 30 or dialysis == "Y":
			print("Ketorolac is contraindicated for this patient. Alternate therapy should be used.")
		else:
			print("The recommended dose for this patient is 15 mg IV every 6 hours OR 10 mg PO every 6 hours. Therapy should not exceed 5 days.")
	elif drug == "levofloxacin" or drug == "levaquin":
		regdose = int(input("Without regard for renal function please input the desired dose (750/500/250): "))
		load = None
		dose = None
		interval = None
		if regdose == 750:
			if crcl > 49 and dialysis == "N":
				dose = 750
				interval = 24
			if 20 <= crcl <=49 and dialysis == "N":
				dose = 750
				interval = 48
			if crcl < 20 or dialtype == "HD" or dialtype == "PD":
				load = 750
				dose = 500
				interval = 48
			if dialtype == "CRRT":
				load = 750
				dose = 250
				interval = 24
		if regdose == 500:
			if crcl > 49 and dialysis == "N":
				dose = 500
				interval = 24
			if 20 <= crcl <=49 and dialysis == "N":
				load = 500
				dose = 250
				interval = 24
			if crcl < 20 or dialysis == "Y":
				load = 500
				dose = 250
				interval = 48
		if regdose == 250:
			if crcl >= 20 and dialysis == "N":
				dose = 250
				interval = 24
			if crcl < 20 and dialysis == "N":
				dose = 250
				interval = 48
			if dialysis == "Y":
				load = 500
				dose = 250
				interval = 48
		if type(load) == int or type(load) == float:
			print(f'This patient should receive {load} on Day 1, then {dose} every {interval} starting on Day {1+(interval/24)}.')
		else:
			print(f'This patient should receive {dose} every {interval} hours.')
	elif drug == "oseltamivir" or drug == "tamiflu":
		load = None
		dose = None
		interval = None
		indication = int(input("Is the indication (1) prophylaxis or (2) treatment?: "))
		if indication != 1 and indication != 2:
			indication = int(input("Please enter a number. Is the indication (1) prophylaxis or (2) treatment?: "))
		if indication == 1:
			if dialysis == "N":
				if crcl > 60:
					dose = 75
					interval = 24
				if 30 <= crcl <= 60:
					dose = 30
					interval = 24
				if crcl < 30:
					dose = 30
					interval = 24
			if dialysis == "Y":
				if dialtype == "HD":
					print("This patient should receive 30 mg after every other dialysis session for the duration of prophylaxis.")
				if dialtype == "PD":
					print("This patient should receive 30 mg now and then 30 mg weekly for the duration of prophylaxis.")
				if dialtype == "CRRT":
					dose = 30
					interval = 24
		if indication == 2:
			if dialysis == "N":
				if crcl > 60:
					dose = 75
					interval = 12
				if 30 <= crcl <= 60:
					dose = 30
					interval = 12
				if crcl < 30:
					dose = 30
					interval = 24
			if dialysis == "Y":
				if dialtype == "HD":
					print("This patient should receive 30 mg after every dialysis session for the duration of treatment.")
				if dialtype == "PD":
					print("This patient should receive 30 mg once.")
				if dialtype == "CRRT":
					dose = 30
					interval = 24
		if (type(dose) == int or type(dose) == float) and (type(interval) == int or type(interval) == float):
			print(f'This patient should receive {dose} mg every {interval} hours.')
	elif drug == "meropenem" or drug == "merrem":
		load = None
		dose = None
		interval = None
		indication = int(input("Is the indication (1) CF/CNS/Meningitis or (2) standard?: "))
		if indication != 1 and indication != 2:
			indication = int(input("Please enter a number. Is the indication (1) CF/CNS/Meningitis or (2) standard?: "))
		if indication == 1:
			if dialysis == "N":
				if crcl > 50:
					dose = "2 "
					interval = 8
				if 26 <= crcl <= 50:
					dose = "2 "
					interval = 12
				if 10 <= crcl < 26:
					dose = "1 "
					interval = 12
				if crcl < 10:
					dose = "1 "
					interval = 24
			if dialysis == "Y":
				if dialtype == "HD":
					print("This patient should receive 1 g IV every 24 hours. This medication should be given after dialysis on dialysis days.")
				if dialtype == "PD":
					dose = "2 "
					interval = 24
				if dialtype == "CRRT":
					dose = "2 "
					interval = 12
		if indication == 2:
			if dialysis == "N":
				if crcl > 50:
					dose = "1 "
					interval = 8
				if 26 <= crcl <= 50:
					dose = "1 "
					interval = 12
				if 10 <= crcl < 26:
					dose = "500 m"
					interval = 12
				if crcl < 10:
					dose = "500 m"
					interval = 24
			if dialysis == "Y":
				if dialtype == "HD":
					print("This patient should receive 500 mg IV every 24 hours. This medication should be given after dialysis on dialysis days.")
				if dialtype == "PD":
					dose = "1 "
					interval = 24
				if dialtype == "CRRT":
					dose = "1 "
					interval = 12
			if type(interval) == int or type(interval) == float:
				print(f'This patient should receive {dose}g IV every {interval} hours.')
	elif drug == "penicillin G" or drug == "penicillin":
		load = None
		dose = None
		interval = None
		if dialysis == "N":
			if crcl > 50:
				dose = 4
				interval = 4
			if 10 <= crcl <= 50:
				dose = 3
				interval = 4
			if crcl < 10:
				load = 4
				dose = 2
				interval = 8
		if dialysis == "Y":
			if dialtype == "HD" or "CRRT":
				load = 4
				dose = 2
				interval = 4
			if dialtype == "PD":
				dose = 2
				interval = 4
		if type(load) == int or type(load) == float:
			print(f'This patient should receive a loading dose of {load} MU, followed by {dose} every {interval} hours. Dosing may change based on severity of infection. The maintenance dose should be {(dose/4):%} of the standard dose.')
		else:
			print(f'This patient should receive {dose} MU every {interval} hours.  Dosing may change based on severity of infection. The dose should be {(dose/4):%} of the standard dose.')
	elif drug == "piperacillin-tazobactam" or drug == "piperacillin" or drug == "tazobactam" or drug == "zosyn":
		load = None
		dose = None
		interval = None
		admin = int(input("Is the administration time (1) extended or (2) traditional?: "))
		if admin != 1 and admin != 2:
			admin = int(input("Please enter a number. Is the administration time (1) extended or (2) traditional?: "))
		if admin == 1:
			if crcl >= 20 and dialysis == "N":
				dose = "3.375-4.5"
				interval = 8
			if crcl < 20 or dialtype == "HD" or dialtype == "PD":
				dose = 3.375
				interval = 12
			if dialtype == "CRRT":
				dose = 3.375
				interval = 8
		if admin == 2:
			if crcl >= 100 and dialysis == "N":
				print("Extended infusion is preferred in this population.")
			if 40 <= crcl < 100 and dialysis == "N":
				dose = 3.375
				interval = 6
			if 20 <= crcl < 40 and dialysis == "N":
				dose = 2.25
				interval = 6
			if crcl < 20 and dialysis == "N":
				dose = 2.25
				interval = 8
			if dialysis == "Y":
				if dialtype == "HD":
					print("This patient should receive 4.5 g every 12 hours or 2.25 g every 8 hours. Administration after dialysis is recommended but not required.")
				if dialtype == "PD":
					print("This patient should receive 4.5 g every 12 hours or 2.25 g every 8 hours.")
				if dialtype == "CRRT":
					print("This patient should receive 4.5 g every 8 hours or 4.5 g loading dose followed by 2.25 g every 6 hours.")
		if type(interval) == int or type(interval) == float:
			if admin == 1:
				inf = "4 hours"
			if admin == 2:
				inf = "30 minutes"
			print(f'This patient should receive {dose} g over {inf} every {interval} hours.')
	elif drug == "rivaroxaban" or drug == "xarelto":
		if dialysis == "Y" or crcl < 15:
			print("Warfarin (Coumadin) or apixaban (Eliquis) are preferred in this patient population.")
		else:
			load = None
			dose = None
			interval = None
			indication = int(input("Is the indication (1) DVT/PE, (2) non-valvular atrial fibrillation, (3) stable CAD or chronic PAD, or (4) VTE prophylaxis or indefinite anticoagulationafter 6 months of therapeutic anticoagulation?: "))
			if indication != 1 and indication != 2 and indication != 3 and indication != 4:
				indication = int(input("Please enter a number. Is the indication (1) DVT/PE, (2) non-valvular atrial fibrillation, (3) stable CAD or chronic PAD, or (4) VTE prophylaxis or indefinite anticoagulationafter 6 months of therapeutic anticoagulation?: "))
			if indication == 1:
				if crcl >= 30:
					print("This patient should receive 15 mg twice daily for 21 days and then 20 mg daily.")
				if 15 <= crcl < 30:
					print("This patient should receive 15 mg twice daily for 21 days and then 20 mg daily. There is limited data to support use in this patient population.")
			if indication == 2:
				if crcl > 50:
					print("This patient should receive 20 mg once daily.")
				if 15 <= crcl <= 50:
					print("This patient should receive 15 mg once daily.")
			if indication == 3:
				print("This patient should receive 2.5 mg twice daily. Low dose aspirin should be included in the regimen.")
			if indication == 4:
				if crcl >= 30:
					print("This patient should receive 10 mg once daily.")
				if 15 <= crcl < 30:
					print("This patient should receive 10 mg once daily. There is limited data to support use in this patient population.")
	elif drug == "vancomycin" or drug == "vancocin":
		load = None
		dose = None
		interval = None
		if dialysis == "N":
			if crcl >= 100:
				dose = 15
				interval = "8-12"
			if 50 <= crcl < 100:
				dose = 15
				interval = 12
			if 30 <= crcl < 50:
				dose = 15
				interval = 24
			else:
				dose = "15-20"
				print("This patient should receive 15-20 mg/kg once and then further doses as determined by serum levels.")
		if dialysis == "Y":
			dose = "15-20"
			print("This patient should receive 15-20 mg/kg once and then further doses as determined by serum levels.")
		if interval != None and dose != None:
				print(f'This patient should receive {dose} mg/kg IV every {interval} hours.')
		ans = str.upper(input("Would you like to calculate your patient's dose? (Y/N): "))
		if ans == "N":
			print("Program end.")
		if ans == "Y":
			if type(dose) == int or type(dose) == float:
				weight = float(input("Enter patient weight (kg): "))
				height = float(input("Enter patient height (in): "))
				sex = input("Enter patient sex (M/F): ")
				if sex == "M":
					ibw = 50 + (2.3 * (height - 60))
				if sex == "F":
					ibw = 45.5 + (2.3 * (height - 60))
				if (weight/ibw) >= 1.2:
					print("Using adjusted body weight.")
					abw = ibw + (0.4*(weight-ibw))
					weight = abw
				admindose = weight*dose
				rounded = round(admindose/250)*250
				if type(interval) == int or type(interval) == float:
					print(f'This patient should receive {rounded} mg IV every {interval} hours.')
				else:
					print(f'This patient should receive {rounded} mg IV once and then further dosing should be determined by serum levels.')
		if ans == "Y" and type(dose) != int and type(dose) != float:
			weight = float(input("Enter patient weight (kg): "))
			height = float(input("Enter patient height (in): "))
			sex = input("Enter patient sex (M/F): ")
			if sex == "M":
				ibw = 50 + (2.3 * (height - 60))
			if sex == "F":
				ibw = 45.5 + (2.3 * (height - 60))
			if (weight/ibw) >= 1.2:
				print("Using adjusted body weight.")
				abw = ibw + (0.4*(weight-ibw))
				weight = abw
			loadmindose = weight*lodose
			lorounded = round(loadmindose/250)*250
			hiadmindose = weight*hidose
			hirounded = round(hiadmindose/250)*250
			if type(interval) == int or type(interval) == float:
				print(f'This patient should receive between {lorounded} mg and {hirounded} mg IV every {interval} hours.')
			else:
				print(f'This patient should receive between {lorounded} mg and {hirounded} mg IV once and then further dosing should be determined by serum levels.')
	print("Program end.")