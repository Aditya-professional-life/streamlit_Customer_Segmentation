import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
import plotly.express as px
from sklearn.preprocessing import LabelEncoder
import plotly.graph_objects as go



st.title("E-Commerce Segmentation Suite")
st.image("image.jpg", caption = "Image Created by Dalle-3")
st.header("About the Customer Segmentation:")


paragraph = """
Every day we deal with a vast amount of data. 
Analysing those data is such a big task but also important. 
This webpage demonstrates the segmentation of customers 
of ecommerce websites based on a machine learning 
algorithm namely K-Means Clustering. We have 
collected the data of around 300 customers from an e-commerce website and their total yearly pay on an e-commerce website and then we will analyse it and find 
the number of optimum clusters. Nowadays every 
company is targeting their customers based on the 
available data and trying to find out the behaviours of 
customers like which kind of product most attracts them, 
what they like. Based on that customer’s behaviour
companies are launching their new products. We will use 
the K-Means Clustering Algorithm, a machine learning-based method to find the optimum number of clusters 
and analyze the underlying client segments supported by 
the information provided. In today’s world, it is hard to 
get the customers’ behaviour and categorize the 
customers into different clusters and categories’ 
customers supported their human ecology and shopping 
for behaviour. This could be a crucial side of client 
partition that permits the business to higher target their 
customers increase in sales and modify their products 
according to their targeted customers and launch new 
products. 
"""

st.write(paragraph)


def main():

    st.subheader("Malls Customers Data")

    # Load the CSV file
    # file_path = "C:/Users/raviv/OneDrive/Desktop/deployment/Mall_Customers.csv"  # Use forward slashes or escape backslashes
    df = pd.read_csv("Mall_Customers.csv")
    st.write("Here is the content of the CSV file:")
    st.write(df)


    st.markdown("## Download CSV File")
    st.write("Click below to download the CSV file:")
    st.download_button(
        label="Download CSV",
        data=df.to_csv().encode('utf-8'),
        file_name="Mall_Customers.csv", 
        mime="text/csv"
    )
    st.subheader("Code for Distplot")
    code_snippet = """
# distplot is used to understand the skewness of data
plt.figure(1, figsize=(15, 6))
n = 0
for x in ["Age", "Annual Income (k$)", "Spending Score (1-100)"]:
    n += 1
    plt.subplot(1, 3, n)
    plt.subplots_adjust(hspace=0.5, wspace=0.5)
    sns.distplot(df[x], bins=20)
    plt.title("Distplot of {}".format(x))
plt.show()
"""
    # st.code(code_snippet, language="python")

    st.subheader("Using distplot is used to understand the skewness of data")

    # Display the graph generated by the code
    fig, axs = plt.subplots(1, 3, figsize=(15, 6))
    for i, x in enumerate(["Age", "Annual Income (k$)", "Spending Score (1-100)"]):
        sns.distplot(df[x], bins=20, ax=axs[i])
        axs[i].set_title("Distplot of {}".format(x))
    st.pyplot(fig)

    st.subheader("Using Countplot to understand the Gender distribution")
    code_snippet = """
plt.figure(figsize=(15, 5))
sns.countplot(y="Gender", data=df)
plt.show()
"""
    # st.code(code_snippet, language="python")

    # Display the graph to the user
    plt.figure(figsize=(15, 5))
    sns.countplot(y="Gender", data=df)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()


    st.subheader("Using Violin plot to understand Skewness and Outlers:")
    # Display the code snippet to the user
    code_snippet = """
plt.figure(1, figsize=(15, 7))

n = 0

for col in ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']:  
    n += 1
    plt.subplot(1, 3, n)
    plt.subplots_adjust(hspace=0.5, wspace=0.5)#horizontal and vertical space
    sns.set(style="whitegrid")  
    sns.violinplot(x=col, y='Gender', data=df)  
    plt.ylabel('Gender' if n == 1 else '')  
    plt.title('Violin Plot of {}'.format(col))

plt.show()
"""
    # st.code(code_snippet, language="python")

    # Display the graph to the user
    plt.figure(1, figsize=(15, 7))

    n = 0

    for col in ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']:  
        n += 1
        plt.subplot(1, 3, n)
        plt.subplots_adjust(hspace=0.5, wspace=0.5)#horizontal and vertical space
        sns.set(style="whitegrid")  
        sns.violinplot(x=col, y='Gender', data=df)  
        plt.ylabel('Gender' if n == 1 else '')  
        plt.title('Violin Plot of {}'.format(col))

    st.pyplot()

    st.subheader("Number of Customers in Diffrent Age Groups:")
    code_snippet2 = '''
age_18_25 = df[df['Age'].between(18, 25)]
age_26_35 = df[df['Age'].between(26, 35)]
age_36_45 = df[df['Age'].between(36, 45)]
age_46_55 = df[df['Age'].between(46, 55)]
age_above_55 = df[df['Age'] > 55]

# Define age group labels
agex = ["18-25", "26-35", "36-45", "46-55", "55+"]

# Calculate the number of customers in each age group
agey = [
    len(age_18_25.values),
    len(age_26_35.values),
    len(age_36_45.values),
    len(age_46_55.values),
    len(age_above_55.values)
]

# Create a bar plot
plt.figure(figsize=(15, 6))
sns.barplot(x=agex, y=agey, palette="mako")  # Corrected the palette parameter
plt.title("Number of Customers in Different Age Groups")
plt.xlabel("Age Group")
plt.ylabel("Number of Customers")
plt.show()'''
    # st.code(code_snippet2, language = "python" )

    # Data preprocessing and plotting
    age_18_25 = df[df['Age'].between(18, 25)]
    age_26_35 = df[df['Age'].between(26, 35)]
    age_36_45 = df[df['Age'].between(36, 45)]
    age_46_55 = df[df['Age'].between(46, 55)]
    age_above_55 = df[df['Age'] > 55]

    # Define age group labels
    agex = ["18-25", "26-35", "36-45", "46-55", "55+"]

    # Calculate the number of customers in each age group
    agey = [
        len(age_18_25),
        len(age_26_35),
        len(age_36_45),
        len(age_46_55),
        len(age_above_55)
    ]

    # Create a bar plot
    plt.figure(figsize=(15, 6))
    sns.barplot(x=agex, y=agey, palette="mako")  # Corrected the palette parameter
    plt.title("Number of Customers in Different Age Groups")
    plt.xlabel("Age Group")
    plt.ylabel("Number of Customers")

    # Display the plot
    st.pyplot()

    st.subheader("Using ScatterPlot to understand Annual Income VS Spending Score:")
    code_snippet3 = '''
plt.figure(figsize=(10, 6))
sns.scatterplot(x="Annual Income (k$)", y="Spending Score (1-100)", data=df)
plt.title("Scatter Plot of Annual Income vs Spending Score")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.show()
'''
    # st.code(code_snippet3, language = "python")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="Annual Income (k$)", y="Spending Score (1-100)", data=df)
    plt.title("Scatter Plot of Annual Income vs Spending Score")
    plt.xlabel("Annual Income (k$)")
    plt.ylabel("Spending Score (1-100)")
    st.pyplot()


    st.subheader("Understanding Age vs Spending Score:")

    code_snippet4 = '''
ss_1_20 = df["Spending Score (1-100)"][(df["Spending Score (1-100)"] >= 1) & (df["Spending Score (1-100)"] <= 20)]
ss_21_40 = df["Spending Score (1-100)"][(df["Spending Score (1-100)"] >= 21) & (df["Spending Score (1-100)"] <= 40)]
ss_41_60 = df["Spending Score (1-100)"][(df["Spending Score (1-100)"] >= 41) & (df["Spending Score (1-100)"] <= 60)]
ss_61_80 = df["Spending Score (1-100)"][(df["Spending Score (1-100)"] >= 61) & (df["Spending Score (1-100)"] <= 80)]
ss_81_100 = df["Spending Score (1-100)"][(df["Spending Score (1-100)"] >= 81) & (df["Spending Score (1-100)"] <= 100)]

# Define score ranges
ssx = ["1-20", "21-40", "41-60", "61-80", "81-100"]

# Count the number of customers in each score range
ssy = [
    len(ss_1_20.values),
    len(ss_21_40.values),
    len(ss_41_60.values),
    len(ss_61_80.values),
    len(ss_81_100.values)
]

# Create a bar plot
plt.figure(figsize=(15, 6))
sns.barplot(x=ssx, y=ssy, palette="rocket")
plt.title("Spending Scores")
plt.xlabel("Score Range")
plt.ylabel("Number of Customers Having the Score")
plt.show()'''
    # st.code(code_snippet4,language = "python")
    ss_1_20 = df["Spending Score (1-100)"][(df["Spending Score (1-100)"] >= 1) & (df["Spending Score (1-100)"] <= 20)]
    ss_21_40 = df["Spending Score (1-100)"][(df["Spending Score (1-100)"] >= 21) & (df["Spending Score (1-100)"] <= 40)]
    ss_41_60 = df["Spending Score (1-100)"][(df["Spending Score (1-100)"] >= 41) & (df["Spending Score (1-100)"] <= 60)]
    ss_61_80 = df["Spending Score (1-100)"][(df["Spending Score (1-100)"] >= 61) & (df["Spending Score (1-100)"] <= 80)]
    ss_81_100 = df["Spending Score (1-100)"][(df["Spending Score (1-100)"] >= 81) & (df["Spending Score (1-100)"] <= 100)]

    # Define score ranges
    ssx = ["1-20", "21-40", "41-60", "61-80", "81-100"]

    # Count the number of customers in each score range
    ssy = [
        len(ss_1_20.values),
        len(ss_21_40.values),
        len(ss_41_60.values),
        len(ss_61_80.values),
        len(ss_81_100.values)
    ]

    # Create a bar plot
    plt.figure(figsize=(15, 6))
    sns.barplot(x=ssx, y=ssy, palette="rocket")
    plt.title("Spending Scores")
    plt.xlabel("Score Range")
    plt.ylabel("Number of Customers Having the Score")
    st.pyplot()

    st.header("Applying K-Means Clustering to Find Optimal number of Segements:")

    code_snippet5 ='''
from sklearn.cluster import KMeans

# Assuming you have a DataFrame named 'df'

X1 = df.loc[:, ["Age", "Spending Score (1-100)"]].values
# Extracts the features "Age" and "Spending Score (1-100)" from the DataFrame df and converts them into a NumPy array X1.
#These features will be used for clustering
wcss = []
#within-cluster sum of squares (WCSS)

for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, init="k-means++")
    kmeans.fit(X1)
    wcss.append(kmeans.inertia_)
    # which is a measure of how internally coherent clusters are. 
#     Inertia quantifies the compactness of the clusters. 
#     Here's a bit more detail:

plt.figure(figsize=(12, 6))
plt.grid()
plt.plot(range(1, 11), wcss, linewidth=2, color="red", marker="8")
plt.xlabel("K Value")
plt.ylabel("WCSS")
plt.title("Elbow Method for Optimal Number of Clusters")
plt.show()'''

    # st.code(code_snippet5, language = "python")


# Assuming you have a DataFrame named 'df'

    X1 = df.loc[:, ["Age", "Spending Score (1-100)"]].values
    # Extracts the features "Age" and "Spending Score (1-100)" from the DataFrame df and converts them into a NumPy array X1.
    #These features will be used for clustering
    wcss = []
    #within-cluster sum of squares (WCSS)

    for k in range(1, 11):
        kmeans = KMeans(n_clusters=k, init="k-means++")
        kmeans.fit(X1)
        wcss.append(kmeans.inertia_)
        # which is a measure of how internally coherent clusters are. 
    #     Inertia quantifies the compactness of the clusters. 
    #     Here's a bit more detail:

    plt.figure(figsize=(12, 6))
    plt.grid()
    plt.plot(range(1, 11), wcss, linewidth=2, color="red", marker="8")
    plt.xlabel("K Value")
    plt.ylabel("WCSS")
    plt.title("Elbow Method for Optimal Number of Clusters")
    st.pyplot()
    kmeans = KMeans(n_clusters  = 5)
    label = kmeans.fit_predict(X1)
    # st.write(label)
    cluster_centers_df = pd.DataFrame(kmeans.cluster_centers_, columns=["X", "Y"])

    # Display the DataFrame with Streamlit
    st.subheader("The coordinates of center of clusters in k= 5")
    st.write(cluster_centers_df)

    st.subheader("The clusters formed by taking Spending Score and Annual Income")

    code_snippet6='''
plt.scatter(X2[:,0], X2[:,1],c = kmeans.labels_,cmap = "rainbow")
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],color = "black")
plt.title("Clusters of Customers")
plt.xlabel("Annual Income(K$)")
plt.ylabel("Spending Score(1-100)")
plt.show()'''

    # st.code(code_snippet6, language = "python")
    X2 = df.loc[:, ["Annual Income (k$)", "Spending Score (1-100)"]].values
    plt.scatter(X2[:,0], X2[:,1],c = kmeans.labels_,cmap = "rainbow")
    plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],color = "black")
    plt.title("Clusters of Customers")
    plt.xlabel("Annual Income(K$)")
    plt.ylabel("Spending Score(1-100)")
    st.pyplot()
    st.subheader("3D clusters visualiztion of Age vs Spending score vs Annual Income:")

# Assuming you have a DataFrame named 'df' and X3 is defined as mentioned before
    X3 = df[["Age", "Annual Income (k$)", "Spending Score (1-100)"]].values

    kmeans = KMeans(n_clusters=5)  # Specify the number of clusters
    clusters = kmeans.fit_predict(X3)
    df["label"] = clusters

    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(111, projection="3d")

    # Define colors for each cluster
    colors = ["blue", "red", "green", "purple", "orange"]

    # Scatter points for each cluster
    for i in range(5):
        ax.scatter(
            df["Age"][df["label"] == i],
            df["Annual Income (k$)"][df["label"] == i],
            df["Spending Score (1-100)"][df["label"] == i],
            c=colors[i],
            s=60,
            label=f"Cluster {i}"
        )

    ax.view_init(30, 185)

    ax.set_xlabel("Age")
    ax.set_ylabel("Annual Income (k$)")
    ax.set_zlabel("Spending Score (1-100)")

    plt.legend()
    st.pyplot()

    st.subheader("Interactive plot")

    X3 = df[["Age", "Annual Income (k$)", "Spending Score (1-100)"]].values

    kmeans = KMeans(n_clusters=5)  # Specify the number of clusters
    clusters = kmeans.fit_predict(X3)
    df["label"] = clusters

    # Define colors for each cluster
    colors = ["blue", "red", "green", "purple", "orange"]
    df['color'] = df['label'].apply(lambda label: colors[label])

    # Plot interactive 3D scatter plot
    fig = px.scatter_3d(df, x='Age', y='Annual Income (k$)', z='Spending Score (1-100)',
                        color='color', symbol='label', size_max=10, opacity=0.7)

    fig.update_layout(
        scene=dict(
            xaxis_title='Age',
            yaxis_title='Annual Income (k$)',
            zaxis_title='Spending Score (1-100)'
        )
    )

    # Display the plot in Streamlit
    st.plotly_chart(fig)

# Assuming you have a DataFrame named 'df' containing the data
    st.subheader("Clusters based on Gender")
# Apply label encoding to 'Gender'
    label_encoder = LabelEncoder()
    df['Gender'] = label_encoder.fit_transform(df['Gender'])

    # Final 3D data
    X = df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)', 'Gender']].values

    # Separate data for male and female
    X_male = X[X[:, -1] == 1][:, :-1]  # Selecting all columns except 'Gender' for males
    X_female = X[X[:, -1] == 0][:, :-1]  # Selecting all columns except 'Gender' for females

    # Perform K-Means clustering for male
    kmeans_male = KMeans(n_clusters=5)
    labels_male = kmeans_male.fit_predict(X_male)

    # Perform K-Means clustering for female
    kmeans_female = KMeans(n_clusters=5)
    labels_female = kmeans_female.fit_predict(X_female)

    # Visualize clusters for male
    fig = plt.figure(figsize=(12, 6))
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.scatter(X_male[:, 0], X_male[:, 1], X_male[:, 2], c=labels_male, cmap='viridis', s=50)
    ax1.set_title('Clusters for Male')
    ax1.set_xlabel('Age')
    ax1.set_ylabel('Annual Income (k$)')
    ax1.set_zlabel('Spending Score (1-100)')

    # Visualize clusters for female
    ax2 = fig.add_subplot(122, projection='3d')
    ax2.scatter(X_female[:, 0], X_female[:, 1], X_female[:, 2], c=labels_female, cmap='viridis', s=50)
    ax2.set_title('Clusters for Female')
    ax2.set_xlabel('Age')
    ax2.set_ylabel('Annual Income (k$)')
    ax2.set_zlabel('Spending Score (1-100)')

    st.pyplot()

    
# Assuming you have a DataFrame named 'df' containing the data
    st.subheader("Comparsion of Male and Female Cluster:")
# Apply label encoding to 'Gender'
    label_encoder = LabelEncoder()
    df['Gender'] = label_encoder.fit_transform(df['Gender'])

    # Final 3D data
    X = df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)', 'Gender']].values

    # Separate data for male and female
    male_data = X[X[:, -1] == 1][:, :-1]  # Selecting all columns except 'Gender' for males
    female_data = X[X[:, -1] == 0][:, :-1]  # Selecting all columns except 'Gender' for females

    # Perform K-Means clustering for male
    kmeans_male = KMeans(n_clusters=5)
    labels_male = kmeans_male.fit_predict(male_data)

    # Perform K-Means clustering for female
    kmeans_female = KMeans(n_clusters=5)
    labels_female = kmeans_female.fit_predict(female_data)

    # Calculate cluster characteristics for Male
    male_cluster_stats = pd.DataFrame(male_data, columns=['Age', 'Annual Income (k$)', 'Spending Score (1-100)'])
    male_cluster_stats['Cluster'] = labels_male
    male_cluster_stats = male_cluster_stats.groupby('Cluster').agg(['mean', 'median', 'std'])
    print("Male Cluster Characteristics:")
    print(male_cluster_stats)

    # Calculate cluster characteristics for Female
    female_cluster_stats = pd.DataFrame(female_data, columns=['Age', 'Annual Income (k$)', 'Spending Score (1-100)'])
    female_cluster_stats['Cluster'] = labels_female
    female_cluster_stats = female_cluster_stats.groupby('Cluster').agg(['mean', 'median', 'std'])
    print("\nFemale Cluster Characteristics:")
    print(female_cluster_stats)

    # Visualize the comparison
    fig, axs = plt.subplots(2, 3, figsize=(18, 10))

    # Plot histograms for Age
    axs[0, 0].hist([male_data[:, 0], female_data[:, 0]], bins=20, color=['blue', 'pink'], label=['Male', 'Female'])
    axs[0, 0].set_title('Age Distribution')
    axs[0, 0].legend()

    # Plot histograms for Annual Income
    axs[0, 1].hist([male_data[:, 1], female_data[:, 1]], bins=20, color=['blue', 'pink'], label=['Male', 'Female'])
    axs[0, 1].set_title('Annual Income Distribution')
    axs[0, 1].legend()

    # Plot histograms for Spending Score
    axs[0, 2].hist([male_data[:, 2], female_data[:, 2]], bins=20, color=['blue', 'pink'], label=['Male', 'Female'])
    axs[0, 2].set_title('Spending Score Distribution')
    axs[0, 2].legend()

    # Plot box plots for Age
    axs[1, 0].boxplot([male_data[:, 0], female_data[:, 0]], labels=['Male', 'Female'])
    axs[1, 0].set_title('Age Box Plot')

    # Plot box plots for Annual Income
    axs[1, 1].boxplot([male_data[:, 1], female_data[:, 1]], labels=['Male', 'Female'])
    axs[1, 1].set_title('Annual Income Box Plot')

    # Plot box plots for Spending Score
    axs[1, 2].boxplot([male_data[:, 2], female_data[:, 2]], labels=['Male', 'Female'])
    axs[1, 2].set_title('Spending Score Box Plot')

    plt.tight_layout()
    st.pyplot()
    st.markdown("### Insights:")
    st.markdown("* **Age Distribution:** Male clusters tend to have a slightly higher median age, while female clusters exhibit a more concentrated age distribution.")
    st.markdown("* **Annual Income:** Male clusters show a wider range of annual incomes, whereas female clusters display a more uniform distribution.")
    st.markdown("* **Spending Score:** Some male clusters demonstrate higher spending scores compared to female clusters, which generally exhibit a more balanced distribution.")
    st.markdown("* **Cluster Characteristics:** Male clusters encompass a mix of high and low-income earners with varied spending behaviors, while female clusters tend to show more consistent spending patterns.")




if __name__ == "__main__":
    main()
