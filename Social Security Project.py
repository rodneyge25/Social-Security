import matplotlib.pyplot as plt

from PIL import Image
#from PIL import Image

#First we ask the user what their income would be at 62, 66, and 70. We also ask for how far into the future they want to look and how much they plan to contribute. 
print("Today we will help you find your most profitable path for your retirement. We will need you to provide your Social Security Income for the ages 62, 66, and 70. We will show you the different outlooks for any distance into the future you would like to see.")
print()
income62 = float(input("How much income would you receive per month starting at age 62? "))
income66 = float(input("How much income would you receive per month starting at age 66? "))
income70 = float(input("How much income would you receive per month starting at age 70? "))

# Here we ask the user for what age they want to look at and how much they plan to contribute each month so we have those numbers for our formulas
futureAge = int(input("What age into your future would you like to look at? "))
contributions = float(input("What percent of your income do you plan on investing (Enter as decimal)? "))

# Next, we find the number of years for each age so we can use that for our formulas
yearsFor62 = futureAge - 62
yearsFor66 = futureAge - 66
yearsFor70 = futureAge - 70

# We find the total income for each age when not investing here
totalIncome62 = income62 * yearsFor62 * 12
totalIncome66 = income66 * yearsFor66 * 12
totalIncome70 = income70 * yearsFor70 * 12

# Here we create for variables for our compund interest equation
rateOfReturn = 0.10
numTimesCompounded = 1
monthlyContributions62 = income62 * contributions
monthlyContributions66 = income66 * contributions
monthlyContributions70 = income70 * contributions

# In these loops we find the total amount of money while investing after the number of years the user asked for
x = 0
while x < (yearsFor62*12):
    x += 1
    totalIncome62Invested = income62 * ((1+(rateOfReturn/numTimesCompounded))**(numTimesCompounded*(1/12)))
    income62 = totalIncome62Invested
    income62 = income62 + monthlyContributions62
totalIncome62Invested += monthlyContributions62

y = 0
while y < (yearsFor66*12):
    y += 1
    totalIncome66Invested = income66 * ((1+(rateOfReturn/numTimesCompounded))**(numTimesCompounded*(1/12)))
    income66 = totalIncome66Invested
    income66 = income66 + monthlyContributions66
totalIncome66Invested += monthlyContributions66

z = 0
for z in range(0, (yearsFor70*12)):
    z += 1
    totalIncome70Invested = income70 * ((1+(rateOfReturn/numTimesCompounded))**(numTimesCompounded*(1/12)))
    income70 = totalIncome70Invested
    income70 = income70 + monthlyContributions70
totalIncome70Invested += monthlyContributions70

print(totalIncome62Invested)

# Here we get our lists set up for the graph
labels = ['Total at 62', 'Total at 66', 'Total at 70', 'Total at 62 (Investing)', 'Total at 66 (Investing)', 'Total at 70 (Investing)']
xAxis = []
totals = [totalIncome62, totalIncome66, totalIncome70, totalIncome62Invested, totalIncome66Invested, totalIncome70Invested]
for index in labels:
    xAxis.append(index)

    
print(totalIncome62Invested)

# Here is the setup to have the graph function properly
plt.bar(xAxis, totals, color=['blue', 'red', 'green'])
plt.xlabel('Age')
plt.ylabel('Total Earnings')
plt.title('Total Earnings from Social Security Until Age {}'.format(futureAge))
plt.show()

# Here we import an image and then manipulate it
image = Image.open("ThumbUp.jpg")
width = image.width
height = image.height

pixels = image.load()
for c in range(0, width):
    for r in range(0, height):
        colors = list(pixels[c, r])
        red = colors[0]
        green = colors[1]
        blue = colors[2]

image.show()

newImage = Image.new("RGB", (width, height))
newPixels = newImage.load()
for c in range(width):
    for r in range(height):
        colors = list(pixels[c,r])
        red = colors[0]
        green = colors[1]
        blue = colors[2]
        newRed = int(0.393*red + 0.769*green + 0.189*blue)
        newGreen = int(0.349*red + 0.686*green + 0.168*blue)
        newBlue = int(0.272*red + 0.534*green + 0.131*blue)        
        newPixels[c,r] = (newRed,newGreen,newBlue)
newImage.show()

redSum=0
greenSum=0
blueSum=0
pixelCount=0

for c in range(width):
    for r in range(height):
        pixelCount += 1
        colors = list(pixels[c,r])
        redSum += colors[0]
        greenSum += colors[1]
        blueSum += colors[2]
        

#Here we ask the user what age he would like to look at by itself
incomes = [income62, income66, income70]
ages = ['62', '66', '70']
searchAge = input('What age would you like to look at by itself? ')
found = False
foundAge = 0
foundIncome = 0
foundIncomeInvesting = 0
index = 0
while found == False and index < len(incomes):
    if searchAge == ages[index]:
        found = True
        foundAge = ages[index]
        if foundAge == "62":
            foundIncome = totalIncome62
            foundIncomeInvesting = totalIncome62Invested
        elif foundAge == "66":
            foundIncome = totalIncome66
            foundIncomeInvesting = totalIncome66Invested
        else:
            foundIncome = totalIncome70
            foundIncomeInvesting = totalIncome70Invested
    else:
        index += 1
#Here we find the most profitable option
maxIncome = 0
for index in range(len(ages)):
    if incomes[index] > maxIncome:
        maxIncome = incomes[index]
print("Looking at age, {}, by itself, you would have {:.2f} without investing and {:.2f} with investing. ".format(searchAge, foundIncome, foundIncomeInvesting))
print()
print("If you play your cards right, you can end up with {:.2f} at age {}.".format(maxIncome, futureAge))
