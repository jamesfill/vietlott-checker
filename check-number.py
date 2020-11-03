import random
import sys
import argparse, logging, os, sys


# Declare logger
logger = logging.getLogger(os.path.basename(__file__))
logger.setLevel(logging.DEBUG)

# Define log format, logger.info to console
formatter = logging.Formatter('%(asctime)s %(name)s #%(lineno)d %(levelname)s: %(message)s', datefmt='%d-%b-%y %H:%M:%S')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
handler.setLevel(logging.INFO)
logger.addHandler(handler)

parser = argparse.ArgumentParser()
parser.add_argument('--number',
										required = False,
										help = 'enter your number')
parser.add_argument('--file',
										required = False,
										help = 'import your file number')
args = parser.parse_args()

if args.number and args.file:
	logger.warning("You need to use either --number or --file to check your number")
	sys.exit(1)

lucky = []

luckyNumber = input("Please enter your provider number: ").strip()
lucky.append(luckyNumber)
lucky = lucky[0].split(" ")

if args.number:
	myNUmber = []
	result = []
	bonus = []
	yourNum = args.number.strip()
	myNUmber.append(yourNum)
	myNUmber = myNUmber[0].split(" ")

	for i in lucky:
		for k in myNUmber:
			if int(k) == int(i):
						result.append(k)
			elif int(k) == int(lucky[-1]):
						bonus.append(k)
			else:
						continue

	resultNumber = ' '.join(result)
	logger.info(f"Reference number: {providerNum}")
	logger.info(f"Your number: {yourNum}")
	logger.info(f"Result: {resultNumber}")

	if len(result) == 6 and not bonus:
		logger.info(f"SUCCESSFUL: Congrast, Jackpot1 with ticket ({yourNum})")
	elif len(result) == 6 and bonus:
		logger.info(f"SUCCESSFUL: Congrast, Jackpot2 with ticket ({yourNum})")
	elif len(result) == 5:
		logger.info(f"SUCCESSFUL: Congrast, you got 40 Mil with ticket ({yourNum})")
	elif len(result) == 4:
		logger.info(f"SUCCESSFUL: Congrast, you got 500k with ticket ({yourNum})")
	elif len(result) == 3:
		logger.info(f"SUCCESSFUL: Congrast, you got 50k with ticket ({yourNum})")
	else:
		logger.warning(f"Your number is not match, try again ?")

elif args.file:

	jackpot1 = []
	jackpot2 = []
	first = []
	second = []
	third = []
	count = 0;

	with open(args.file, 'r') as file:
		for lines in file:
			myNUmber = []
			result = []
			bonus = []
			yourNum = lines.replace("\n", "").strip()
			myNUmber.append(yourNum)
			myNUmber = myNUmber[0].split(" ")
			for i in lucky:
				for k in myNUmber:
					if int(k) == int(i):
								result.append(k)
					elif int(k) == int(lucky[-1]):
								bonus.append(k)
					else:
								continue

			# resultNumber = ' '.join(result)
			# logger.info(f"Reference number: {providerNum}")
			# logger.info(f"Your number: {yourNum}")
			# logger.info(f"Result: {resultNumber}")

			if len(result) == 6 and not bonus:
				logger.info(f"SUCCESSFUL: Congrast, Jackpot1 with ticket ({yourNum})")
			elif len(result) == 6 and bonus:
				logger.info(f"SUCCESSFUL: Congrast, Jackpot2 with ticket ({yourNum})")
			elif len(result) == 5:
				logger.info(f"SUCCESSFUL: Congrast, you got 40 Mil with ticket ({yourNum})")
			elif len(result) == 4:
				logger.info(f"SUCCESSFUL: Congrast, you got 500k with ticket ({yourNum})")
			elif len(result) == 3:
				logger.info(f"SUCCESSFUL: Congrast, you got 50k with ticket ({yourNum})")
			else:
				logger.warning(f"Your number is not match, try again ?")






