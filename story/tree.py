class TreeNode:
    def __init__(self, story_part):
        self.story_part = story_part
        self.choices = []

    def add_child(self, child):
        self.choices.append(child)
        return

    def traverse(self):
        story_node = self
        print(story_node.story_part)
        while len(story_node.coices) != 0:
            choice = input('Enter 1 or 2 to continue to story: ')
            while choice not in ['1', '2']:
                choice = input('Please enter a valid choice (1 or 2): ')
            chosen_index = int(choice) - 1
            chosen_path = story_node.choices[chosen_index]
            print(chosen_path.story_part)
            story_node = chosen_path
