import json
import os

batch_path = ""  # Save path to "Batch_Data" folder in Blend_My_NFTs Output

def getBatchData(a):
    """
    Retrieves a given batches data determined by renderBatch in config.py
    """

    batch = json.load(open(os.path.join(batch_path, a)))

    NFTs_in_Batch = batch["NFTs_in_Batch"]
    hierarchy = batch["hierarchy"]
    BatchDNAList = batch["BatchDNAList"]

    return NFTs_in_Batch, hierarchy, BatchDNAList

def save_batch(batch, file_name):
    saved_batch = json.dumps(batch, indent=1, ensure_ascii=True)

    with open(os.path.join(file_name), 'w') as outfile:
        outfile.write(saved_batch + '\n')


for a in os.listdir(batch_path):
    NFTs_in_Batch, hierarchy, BatchDNAList = getBatchData(a)
    NEW_BatchDNAList = []

    for b in BatchDNAList:
        NEW_BatchDNAList.append({
            b: {"Complete": False}
        })

    batch_new = {
        "NFTs_in_Batch": NFTs_in_Batch,
        "hierarchy": hierarchy,
        "BatchDNAList": NEW_BatchDNAList
    }

    batch_dumped = json.dumps(batch_new, indent=1, ensure_ascii=True)

    with open(os.path.join(batch_path, a), "w") as outfile:
        outfile.write(batch_dumped)
print("Complete")
