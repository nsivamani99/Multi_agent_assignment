class ResourceAgent:
    def collect(self, use_cases):
        # Dummy dataset links
        datasets = {
            "Personalized Product Recommendations": "https://www.kaggle.com/datasets/retail-recommendation",
            "Chatbots for Automated Customer Support": "https://github.com/chatbot-dataset",
            "Inventory Management using Predictive Analytics": "https://huggingface.co/inventory-forecast"
        }
        return datasets
