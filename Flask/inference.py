import torch
from model import DamageModel
from PIL import Image
import torchvision.models as models
from torchvision import transforms

IMAGE_SIZE = (224, 224)

image_transforms = transforms.Compose([
    transforms.Resize(IMAGE_SIZE),
    transforms.ToTensor(),
    transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))
])

class DamageHandler():
    def __init__(self, model_path, classes):
        if torch.cuda.is_available():
            self.device = torch.device('cuda')
        else:
            self.device = torch.device('cpu')

        self.classes = classes
        self.model = DamageModel(models.resnet50(pretrained=False), len(classes)).to(self.device)
        self.model.load_state_dict(torch.load(model_path, map_location=self.device)['state_dict'])

    def predict(self, image_path):
        image = Image.open(image_path)
        image = image_transforms(image).unsqueeze(0)
        with torch.no_grad():
            self.model.eval()
            output = self.model(image.to(self.device)).squeeze()
            print(output, '\n')

        return self.classes[output.argmax()]
