import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def main():
    df = pd.read_csv("evaluator_data.csv")
    print(df.columns)

    fig, axs = plt.subplots(nrows=1)
    sns.set_theme(style="whitegrid")
    g = sns.catplot(
            data=df, kind="bar",
            x="no_of_drones", y="data_size", hue="percentage_of_two_sub",
            ci="sd", palette="dark", alpha=.6, height=6
        )
    g.despine(left=True)
    g.set_axis_labels("#of drones", "data size(KB)")
    g.legend.set_title("")
    plt.tight_layout()
    plt.savefig('evaluator_plot_part1.png')

main()