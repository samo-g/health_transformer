import matplotlib.pyplot as plt
import numpy as np
 
 
# Creating dataset
#np.random.seed(10)
 
EnBERT = (19.52259827,16.51535416,3.203588486,16.50183678,12.57825279,23.54474449,16.69320679,17.45191765,29.39304543,23.12378502,21.51817989,25.50131798,19.17679214,19.4180603,15.75951767,17.40893173,13.25574112)
BigBird = (-17.44336891,-22.48169518,-28.94421768,-29.98841095,-19.49720383,-21.43226242,-27.04055977,-30.1513567,-42.63545418,-27.42898846,-27.86152649,-15.26669312,-21.69108391,-17.63623428,-30.42033005,-20.64208221,-15.23362064)
HealthF = (-8.50282383,-1.059875488,0.1144313812256,-2.264843941,-3.003647804,-4.539916992,-2.525548935,-1.461083412,-4.113545418,-1.901939392,3.347154617,-4.993850708,-7.307497978,-7.05632019,-2.730463028,-4.720329285,-0.135726929)
PhS = (-0.792764664,-5.76496315,0.158212662,-9.133810043,-8.629493713,-10.43291092,-4.981649399,3.439804077,3.241558075,0.436485291,-4.785635948,-7.550010681,-3.891506195,-0.59252739,-1.342050552,7.195556641,-1.104585648)
ZhBert = (-0.427731514,0.673980236,-2.896359444,2.654287338,0.256966591,-0.286241531,2.015494347,0.599594116,-0.723042488,-0.680828571,5.357958794,-0.798129082,0.560865402,1.139697075,-0.016951561,0.088152885,2.614080906,-0.947916985)
ZhHealth = (4.538589478,0.798495293,3.608156204,-0.623163223,4.96043396,3.544959068,1.855365753,3.670120239,0.383638382,5.789780617,1.198210716,1.389944077,3.256931305,2.105034828,1.310212135,3.895372391,-3.820804596,5.7115345)

data = [EnBERT, BigBird, HealthF, PhS, ZhBert, ZhHealth] 
 
fig = plt.figure(figsize =(10, 7))


# Creating axes instance
ax = fig.add_axes([0, 0, 1, 1])

# Creating plot
bp = ax.boxplot(data)
plt.xticks([1, 2, 3, 4, 5, 6], ['EN-BERT', 'EN-BigBird', 'EN-HealthF', 'EN-PhS','ZH-BERT','ZH-Health'])
plt.ylabel("Suprisal True - False")
plt.title("Figure 1. Insert description here") # don't forget to change this
plt.axhline(y=0, color='0.8', linestyle='-')

# Set the font size of ticks and labels # change values depending on rendering on paper
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.rc('axes', labelsize=20)    # fontsize of the x and y labels
plt.rc('axes', titlesize=20)    # fontsize of the title

# show plot
plt.show()