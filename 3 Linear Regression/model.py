import torch.nn as nn

class MultivariateLinearRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(3, 1)

    def forward(self, x):
        return self.linear(x)

class LinearRegressionModel(nn.Module): # torch.nn.Module 상속받는 클래스
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x): # model 객체를 데이터와 호출하면 자동 실행
        return self.linear(x)