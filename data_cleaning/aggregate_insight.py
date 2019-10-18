import rbo

def rboresult(groundtruth, new):
    return rbo.RankingSimilarity(groundtruth, new).rbo()

