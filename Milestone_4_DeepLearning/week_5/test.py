import torch
print(torch.cuda.is_available())
print(torch.version.cuda)      # Should show 12.6
# print(torch.cuda.get_device_name(0))