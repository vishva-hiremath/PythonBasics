# Simplified conceptual structure

class BaseDataLoader:
    def __init__(self, data_path): ...
    def get_next_batch(self): ... # Must be implemented by subclasses

class ImageDataLoader(BaseDataLoader):
    def get_next_batch(self): # Implementation for images
        ...

class BaseModel:
    def __init__(self, config): ...
    def build(self): ... # Must be implemented by subclasses
    def forward(self, batch_data): ... # Must be implemented
    def save(self, path): ...
    def load(self, path): ...

class CNNModel(BaseModel):
    def build(self): # Build CNN layers
        ...
    def forward(self, image_batch): # CNN forward pass
        ...

class Trainer:
    def __init__(self, model, train_loader, val_loader, optimizer, config):
        self.model = model # Can be CNNModel, RNNModel etc. (Polymorphism)
        self.train_loader = train_loader # Can be ImageDataLoader etc. (Polymorphism)
        self.val_loader = val_loader
        self.optimizer = optimizer
        self.config = config

    def train_epoch(self):
        for batch in self.train_loader.get_next_batch():
            output = self.model.forward(batch['data'])
            loss = self.compute_loss(output, batch['labels'])
            # ... backpropagation, optimizer step ...

    def train(self):
        for epoch in range(self.config['epochs']):
            self.train_epoch()
            self.evaluate() # Uses self.model and self.val_loader

    def compute_loss(self, output, target): ...
    def evaluate(self): ...

# --- Main script ---
# config = load_config()
# train_data = ImageDataLoader(config['train_data_path'])
# cnn = CNNModel(config['model_config'])
# adam_opt = AdamOptimizer(config['optimizer_config'])
# trainer = Trainer(model=cnn, train_loader=train_data, ...)
# trainer.train()