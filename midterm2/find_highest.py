def find_highest(class_a_means, class_b_means):
    higher_means = []
    while len(class_a_means) != 0:
        if class_a_means[0] > class_b_means[0]:
            higher_means.append(class_a_means[0])
        else:
            higher_means.append(class_b_means[0])
        del(class_a_means[0])
        del(class_b_means[0])
    return higher_means


def calculate_mean(higher_means):
    total = 0
    for mean in higher_means:
        total += mean
    return total / len(higher_means)


def main():
    class_a_means = [80.0, 73.5, 94.5, 97.4, 84.3, 77.9]
    class_b_means = [97.2, 73.4, 94.5, 84.1, 76.9, 88.3]
    print('The highest quiz scores across the two classes are:')
    higher_means = find_highest(class_a_means, class_b_means)
    print(higher_means)
    print('The overall mean of the highest scores is:')
    print(calculate_mean(higher_means))


main()
