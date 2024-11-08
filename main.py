import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import csv
import sys

def main():
    '''Main function to handle correct input'''
    input = sys.argv
    print(input)
    try:
         iterations = int(input[1])
         if len(input) !=2 :
              raise Exception
    except Exception:
         print("Incorrect format of arguments, your input argument must be a single integer representing the desired # of iterations")
         exit()

    generate_and_visualize(iterations)
    
    

def generate_and_visualize(iterations):
    '''Given a number of iterations, generate normally distributed floating
        point numbers that oscillate between 1 and -1
        Outliers are detected, visualized and stored in a tsv file
    '''
    sigma = 1
    s = []
    anomalies = []
    anomalies_data = []
    # Set up the figure and axis
    fig, ax = plt.subplots()
    ax.set_ylim(-10, 10)  

    # Update function for animation
    def update(iteration):
  
        amplitude =1
        # gradual drift in the mean over time, and oscillate between 0 and 1
        init_mu =amplitude * np.sin(iteration/100)

        # Generate new element after changing mean
        new_element = np.random.normal(init_mu, sigma)
        s.append(new_element)

        # Calculating outliers
        q1, q3 = np.percentile(s, [25, 75])
        IQR = q3-q1
        if new_element > (q3+ 1.5*IQR) or new_element < (q1-1.5*IQR):
            anomalies.append(new_element)
            anomalies_data.append({
                    "outlier_value": round(new_element,5),
                    "related_mean_of_data": round(init_mu,5)
                })
        
        # Write anomaly data to TSV file
        write_dictionary_to_tsv(anomalies_data)

        ax.clear()
        ax.scatter(anomalies, [1] * len(anomalies), color='red')
        ax.boxplot(s, vert=False, patch_artist=True,showfliers=False)
        ax.set_title("Outlier detection")
        ax.set_xlabel("Value")
        ax.set_xlim(-5, 5) 


    animation = FuncAnimation(fig, update, frames=range(iterations), repeat=False, interval=1)
    plt.show()

def write_dictionary_to_tsv(dictionary):
    with open("outlier_data.tsv", "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["outlier_value", "related_mean_of_data"], delimiter='\t')
            writer.writeheader()
            writer.writerows(dictionary)


main()