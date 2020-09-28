import argparse
import os
import pickle

import tqdm

from utils import *

parser = argparse.ArgumentParser()
parser.add_argument('-p', type=str, required=True, help='Path to MPIIGaze Orignal dir')
parser.add_argument('-s', type=str, default='mpiigaze-norm-rgb.pickle',
                    help='Path to save results, is a pickle file')
args = parser.parse_args()

print(args)

full_dict = {}

face_model_path = '6 points-based face model.mat'
face_model = get_facemodel(face_model_path)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

print('start normalize data...')
for person_id in tqdm.tqdm(os.scandir(args.p)):
    calibration_fp = os.path.join(person_id.path, 'Calibration/Camera.mat')
    cameraMatrix = get_cameraMatrix(calibration_fp)
    for day_id in tqdm.tqdm(os.scandir(person_id.path)):
        if 'Calibration' not in day_id.name:
            annotation_file = os.path.join(day_id.path, 'annotation.txt')
            annotation_dict = get_annotation_dict_in_day(annotation_file)
            for img_id in range(len(annotation_dict)):
                img_name = f'{img_id + 1:04}.jpg'
                img_fp = os.path.join(day_id.path, img_name)
                annotation = annotation_dict[img_name]
                result = get_eyes_image(img_fp, annotation, cameraMatrix, face_model, clahe=clahe)
                full_dict[f'{person_id.name}/{day_id.name}/{img_name}'] = result

print(f'start save file at {args.s}...')
with open(args.s, 'wb') as f:
    pickle.dump(full_dict, f)

print('done')
