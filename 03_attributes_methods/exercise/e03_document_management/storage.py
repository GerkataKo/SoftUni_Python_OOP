class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    @staticmethod
    def filtered(id, list):
        filtered = [i for i in list if i.id == id][0]
        return filtered

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        filtered_category = self.filtered(category_id, self.categories)
        if filtered_category:
            filtered_category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        filtered_topic = self.filtered(topic_id, self.topics)
        if filtered_topic:
            filtered_topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        filtered_document = self.filtered(document_id, self.documents)
        if filtered_document:
            filtered_document.edit(new_file_name)

    def delete_category(self, category_id):
        filtered_category = self.filtered(category_id, self.categories)
        if filtered_category:
            self.categories.remove(filtered_category)

    def delete_topic(self, topic_id):
        filtered_topic = self.filtered(topic_id, self.topics)
        if filtered_topic:
            self.topics.remove(filtered_topic)

    def delete_document(self, document_id):
        filtered_document = self.filtered(document_id, self.documents)
        if filtered_document:
            self.documents.remove(filtered_document)

    def get_document(self, document_id):
        filtered_document = self.filtered(document_id, self.documents)
        if filtered_document:
            return repr(filtered_document)

    def __repr__(self):
        result = '\n'.join([repr(d) for d in self.documents])

        return result
