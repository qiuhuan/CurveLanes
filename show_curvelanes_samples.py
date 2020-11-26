import cv2
import json
import os
import pdb

def parse_json(fn):
    data = json.load(open(fn,'r'))
    # print(data.keys())
    lanes = data['Lines']
    # pdb.set_trace()
    lanes_ = []
    for lane in lanes:
        lane = [(float(v['x']), float(v['y'])) for v in lane]
        lanes_.append(lane)
    return lanes_

def show(img_fn, lanes):
    img = cv2.imread(img_fn)
    for lane in lanes:
        x1 = int(lane[0][0])
        y1 = int(lane[0][1])
        for i in range(1,len(lane)):
            x2 = int(lane[i][0])
            y2 = int(lane[i][1])
            cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)
            x1 = x2
            y1 = y2

    img1 = cv2.resize(img,None,fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)
    cv2.imshow('img',img1)
    cv2.waitKey()
    return img


if __name__=='__main__':
    img_dir='train/images'
    labels_dir='train/labels'

    img_fns = os.listdir(img_dir)

    for i,fn in enumerate(img_fns):
        lb_fn = fn.replace('jpg','lines.json')
        lanes = parse_json(os.path.join(labels_dir, lb_fn))

        img = show(os.path.join(img_dir, fn), lanes)
        cv2.imwrite('show_samples/'+fn, img)
        if i>10:
            break
