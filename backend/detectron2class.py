
from config import get_config
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog


class Detectron2Class:
    def __init__(self):
        self.cfg = get_cfg()
        self.cfg.MODEL.DEVICE = 'cpu'
        self.cfg.merge_from_file(model_zoo.get_config_file(get_config()['model-config']))
        self.cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # set threshold for this model
        self.cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url(get_config()['model-config'])
        self.predictor = DefaultPredictor(self.cfg)

    def detect_image(self, image):
        outputs = self.predictor(image)
        v = Visualizer(image[:, :, ::-1], MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0]), scale=1.2)
        out = v.draw_instance_predictions(outputs["instances"].to("cpu"))
        return out.get_image()[:, :, ::-1]