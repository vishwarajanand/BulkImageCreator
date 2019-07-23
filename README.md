# BulkImageCreator
Contains script to create bulk images using python with numbers written on them for easy image identification. These images can be uploaded on GitHub for a web browseable url.

I had created this repo so that I have a tool to create several images for FB catalog testing.


# Usage
`python create_multiple_images.py` - change configs and function params to het different results

# Depemndency on PIL (Python Image Library)
Install as below:
`pip install PIP`

## sample output (after manually uplaoding images to github)

[{"name":"1-1","url":"https://user-images.githubusercontent.com/7369612/61700525-6c368c00-ad6f-11e9-9487-ca1a535ff30b.png"},
{"name":"1-2","url":"https://user-images.githubusercontent.com/7369612/61700526-6c368c00-ad6f-11e9-9f2d-081fa2b78b0a.png"},
{"name":"1-3","url":"https://user-images.githubusercontent.com/7369612/61700531-6ccf2280-ad6f-11e9-9652-aada0b62a998.png"},
{"name":"1-4","url":"https://user-images.githubusercontent.com/7369612/61700533-6ccf2280-ad6f-11e9-9f18-9dff9160d286.png"},
{"name":"1-5","url":"https://user-images.githubusercontent.com/7369612/61700534-6d67b900-ad6f-11e9-804a-81d6a3dabd85.png"},
{"name":"1-6","url":"https://user-images.githubusercontent.com/7369612/61700535-6d67b900-ad6f-11e9-97b6-311ffaac5592.png"},
{"name":"1-7","url":"https://user-images.githubusercontent.com/7369612/61700537-6d67b900-ad6f-11e9-92e7-95af6dda0d15.png"},
{"name":"1-8","url":"https://user-images.githubusercontent.com/7369612/61700538-6d67b900-ad6f-11e9-8621-66008003a802.png"},
{"name":"1-9","url":"https://user-images.githubusercontent.com/7369612/61700539-6e004f80-ad6f-11e9-84cc-e729392dda24.png"},
{"name":"1-10","url":"https://user-images.githubusercontent.com/7369612/61700540-6e004f80-ad6f-11e9-9ac3-c597fa8a8f6c.png"},
{"name":"2-1","url":"https://user-images.githubusercontent.com/7369612/61700541-6e98e600-ad6f-11e9-9508-f9455e2e38cc.png"},
{"name":"2-2","url":"https://user-images.githubusercontent.com/7369612/61700542-6e98e600-ad6f-11e9-8d6c-dfa00e7a5c79.png"},
{"name":"2-3","url":"https://user-images.githubusercontent.com/7369612/61700543-6e98e600-ad6f-11e9-9075-8f0fd4c6d80f.png"},
{"name":"2-4","url":"https://user-images.githubusercontent.com/7369612/61700544-6e98e600-ad6f-11e9-88f6-3069abaf5739.png"},
{"name":"2-5","url":"https://user-images.githubusercontent.com/7369612/61700547-6f317c80-ad6f-11e9-8c9f-d97d32cfeaa8.png"},
{"name":"2-6","url":"https://user-images.githubusercontent.com/7369612/61700548-6fca1300-ad6f-11e9-932d-b75c1a25502f.png"},
{"name":"2-7","url":"https://user-images.githubusercontent.com/7369612/61700549-6fca1300-ad6f-11e9-8814-e295c1c5f186.png"},
{"name":"2-8","url":"https://user-images.githubusercontent.com/7369612/61700553-6fca1300-ad6f-11e9-90c5-7a30f41b939e.png"},
{"name":"2-9","url":"https://user-images.githubusercontent.com/7369612/61700554-7062a980-ad6f-11e9-9fc3-14d115e441cf.png"},
{"name":"2-10","url":"https://user-images.githubusercontent.com/7369612/61700555-7062a980-ad6f-11e9-9ea5-243104d2238c.png"},
{"name":"3-1","url":"https://user-images.githubusercontent.com/7369612/61700557-7062a980-ad6f-11e9-9c13-d756effa5028.png"},
{"name":"3-2","url":"https://user-images.githubusercontent.com/7369612/61700558-70fb4000-ad6f-11e9-875b-4f36492b3cc2.png"},
{"name":"3-3","url":"https://user-images.githubusercontent.com/7369612/61700560-70fb4000-ad6f-11e9-8d20-2169e8c756a2.png"},
{"name":"3-4","url":"https://user-images.githubusercontent.com/7369612/61700561-70fb4000-ad6f-11e9-869e-ac3007a34002.png"},
{"name":"3-5","url":"https://user-images.githubusercontent.com/7369612/61700562-7193d680-ad6f-11e9-982d-779f3646c7c6.png"},
{"name":"3-6","url":"https://user-images.githubusercontent.com/7369612/61700563-7193d680-ad6f-11e9-9e79-d376ff308008.png"},
{"name":"3-7","url":"https://user-images.githubusercontent.com/7369612/61700565-7193d680-ad6f-11e9-9eb9-a83c13aae95d.png"},
{"name":"3-8","url":"https://user-images.githubusercontent.com/7369612/61700567-722c6d00-ad6f-11e9-8dd9-ec9c0df11b9b.png"},
{"name":"3-9","url":"https://user-images.githubusercontent.com/7369612/61700568-722c6d00-ad6f-11e9-9180-6c8b5b4f4ea0.png"},
{"name":"3-10","url":"https://user-images.githubusercontent.com/7369612/61700569-722c6d00-ad6f-11e9-9b60-ca9325e78325.png"},
{"name":"4-1","url":"https://user-images.githubusercontent.com/7369612/61700571-72c50380-ad6f-11e9-9dc2-d7f27b52d78a.png"},
{"name":"4-2","url":"https://user-images.githubusercontent.com/7369612/61700573-72c50380-ad6f-11e9-91f6-1fbd73374b15.png"},
{"name":"4-3","url":"https://user-images.githubusercontent.com/7369612/61700575-72c50380-ad6f-11e9-975d-8c16d17054e4.png"},
{"name":"4-4","url":"https://user-images.githubusercontent.com/7369612/61700576-735d9a00-ad6f-11e9-8306-e1f41a2a3dea.png"},
{"name":"4-5","url":"https://user-images.githubusercontent.com/7369612/61700577-735d9a00-ad6f-11e9-9210-f8cf7fecd50a.png"},
{"name":"4-6","url":"https://user-images.githubusercontent.com/7369612/61700579-735d9a00-ad6f-11e9-902b-4fe268967348.png"},
{"name":"4-7","url":"https://user-images.githubusercontent.com/7369612/61700580-73f63080-ad6f-11e9-91ef-04aac5b55090.png"},
{"name":"4-8","url":"https://user-images.githubusercontent.com/7369612/61700581-73f63080-ad6f-11e9-8416-f948cc6d45d1.png"},
{"name":"4-9","url":"https://user-images.githubusercontent.com/7369612/61700583-73f63080-ad6f-11e9-968e-8dc030106a73.png"},
{"name":"4-10","url":"https://user-images.githubusercontent.com/7369612/61700584-748ec700-ad6f-11e9-9bb8-95271693895a.png"},
{"name":"5-1","url":"https://user-images.githubusercontent.com/7369612/61700586-748ec700-ad6f-11e9-90ac-a7d23ecbf1a7.png"},
{"name":"5-2","url":"https://user-images.githubusercontent.com/7369612/61700587-748ec700-ad6f-11e9-99e9-1ace33cdcb55.png"},
{"name":"5-3","url":"https://user-images.githubusercontent.com/7369612/61700589-75275d80-ad6f-11e9-830c-a141bc9af537.png"},
{"name":"5-4","url":"https://user-images.githubusercontent.com/7369612/61700590-75275d80-ad6f-11e9-9cac-ac1d53ffb93f.png"},
{"name":"5-5","url":"https://user-images.githubusercontent.com/7369612/61700594-75275d80-ad6f-11e9-8b28-65b7b879ef6d.png"},
{"name":"5-6","url":"https://user-images.githubusercontent.com/7369612/61700595-75bff400-ad6f-11e9-8dc1-83819ac3477c.png"},
{"name":"5-7","url":"https://user-images.githubusercontent.com/7369612/61700597-75bff400-ad6f-11e9-8534-73f2bdc4021b.png"},
{"name":"5-8","url":"https://user-images.githubusercontent.com/7369612/61700601-75bff400-ad6f-11e9-9e76-6a32aa413dc2.png"},
{"name":"5-9","url":"https://user-images.githubusercontent.com/7369612/61700602-76588a80-ad6f-11e9-9922-7d9310e5f11b.png"},
{"name":"5-10","url":"https://user-images.githubusercontent.com/7369612/61700604-76588a80-ad6f-11e9-812f-d41550aadf5c.png"},
{"name":"6-1","url":"https://user-images.githubusercontent.com/7369612/61700607-76588a80-ad6f-11e9-9b5f-78a9415c4bec.png"},
{"name":"6-2","url":"https://user-images.githubusercontent.com/7369612/61700608-76f12100-ad6f-11e9-89cb-0a01043d23c4.png"},
{"name":"6-3","url":"https://user-images.githubusercontent.com/7369612/61700611-7789b780-ad6f-11e9-8719-420354461092.png"},
{"name":"6-4","url":"https://user-images.githubusercontent.com/7369612/61700612-7789b780-ad6f-11e9-9b4f-265fa3c3e674.png"},
{"name":"6-5","url":"https://user-images.githubusercontent.com/7369612/61700613-7789b780-ad6f-11e9-9ccd-523ae3613e16.png"},
{"name":"6-6","url":"https://user-images.githubusercontent.com/7369612/61700615-78224e00-ad6f-11e9-8ba1-2c505eed86bd.png"},
{"name":"6-7","url":"https://user-images.githubusercontent.com/7369612/61700617-78224e00-ad6f-11e9-82f3-2e20c03deae3.png"},
{"name":"6-8","url":"https://user-images.githubusercontent.com/7369612/61700621-78224e00-ad6f-11e9-883d-4843419f8259.png"},
{"name":"6-9","url":"https://user-images.githubusercontent.com/7369612/61700624-78bae480-ad6f-11e9-8b42-d2f0252092ca.png"},
{"name":"6-10","url":"https://user-images.githubusercontent.com/7369612/61700625-78bae480-ad6f-11e9-80cc-062008d356ac.png"},
{"name":"7-1","url":"https://user-images.githubusercontent.com/7369612/61700626-78bae480-ad6f-11e9-95d0-3aa0c0d2836c.png"},
{"name":"7-2","url":"https://user-images.githubusercontent.com/7369612/61700628-79537b00-ad6f-11e9-835a-5ac4a444782c.png"},
{"name":"7-3","url":"https://user-images.githubusercontent.com/7369612/61700629-79537b00-ad6f-11e9-9828-36ddc3f1ad27.png"},
{"name":"7-4","url":"https://user-images.githubusercontent.com/7369612/61700631-79ec1180-ad6f-11e9-937e-5c3825da35db.png"},
{"name":"7-5","url":"https://user-images.githubusercontent.com/7369612/61700632-79ec1180-ad6f-11e9-8f18-217d3b51e1c7.png"},
{"name":"7-6","url":"https://user-images.githubusercontent.com/7369612/61700634-79ec1180-ad6f-11e9-8c2f-90e9d1fbbc77.png"},
{"name":"7-7","url":"https://user-images.githubusercontent.com/7369612/61700636-79ec1180-ad6f-11e9-82da-b0998790a6bf.png"},
{"name":"7-8","url":"https://user-images.githubusercontent.com/7369612/61700637-7a84a800-ad6f-11e9-9369-4b3b6f4d508e.png"},
{"name":"7-9","url":"https://user-images.githubusercontent.com/7369612/61700638-7a84a800-ad6f-11e9-9f35-7e994fe24a83.png"},
{"name":"7-10","url":"https://user-images.githubusercontent.com/7369612/61700639-7b1d3e80-ad6f-11e9-9a47-c11270e8a983.png"},
{"name":"8-1","url":"https://user-images.githubusercontent.com/7369612/61700640-7b1d3e80-ad6f-11e9-9692-7dc9e80b979e.png"},
{"name":"8-2","url":"https://user-images.githubusercontent.com/7369612/61700642-7b1d3e80-ad6f-11e9-9f46-69d80fa5ad1a.png"},
{"name":"8-3","url":"https://user-images.githubusercontent.com/7369612/61700644-7bb5d500-ad6f-11e9-96c9-e48457763e73.png"},
{"name":"8-4","url":"https://user-images.githubusercontent.com/7369612/61700645-7bb5d500-ad6f-11e9-9c63-af1e6e7f0810.png"},
{"name":"8-5","url":"https://user-images.githubusercontent.com/7369612/61700646-7bb5d500-ad6f-11e9-960d-ba89d9d0dea0.png"},
{"name":"8-6","url":"https://user-images.githubusercontent.com/7369612/61700648-7c4e6b80-ad6f-11e9-91b6-4ea05901e975.png"},
{"name":"8-7","url":"https://user-images.githubusercontent.com/7369612/61700649-7c4e6b80-ad6f-11e9-80a0-19781e66d00a.png"},
{"name":"8-8","url":"https://user-images.githubusercontent.com/7369612/61700650-7c4e6b80-ad6f-11e9-8a2d-96f47056dd7a.png"},
{"name":"8-9","url":"https://user-images.githubusercontent.com/7369612/61700652-7ce70200-ad6f-11e9-978c-b3e578251deb.png"},
{"name":"8-10","url":"https://user-images.githubusercontent.com/7369612/61700653-7ce70200-ad6f-11e9-906e-09065e8e3a98.png"},
{"name":"9-1","url":"https://user-images.githubusercontent.com/7369612/61700654-7ce70200-ad6f-11e9-80a9-b3857b8f5674.png"},
{"name":"9-2","url":"https://user-images.githubusercontent.com/7369612/61700655-7d7f9880-ad6f-11e9-9af0-124b19a9c04c.png"},
{"name":"9-3","url":"https://user-images.githubusercontent.com/7369612/61700656-7d7f9880-ad6f-11e9-8e42-5c3e14e3d6a9.png"},
{"name":"9-4","url":"https://user-images.githubusercontent.com/7369612/61700657-7d7f9880-ad6f-11e9-8649-8c9deae00e06.png"},
{"name":"9-5","url":"https://user-images.githubusercontent.com/7369612/61700658-7e182f00-ad6f-11e9-9803-512fa92c3ef2.png"},
{"name":"9-6","url":"https://user-images.githubusercontent.com/7369612/61700659-7e182f00-ad6f-11e9-8ca4-83568bca20dc.png"},
{"name":"9-7","url":"https://user-images.githubusercontent.com/7369612/61700660-7e182f00-ad6f-11e9-8f45-b5da066efd8d.png"},
{"name":"9-8","url":"https://user-images.githubusercontent.com/7369612/61700661-7eb0c580-ad6f-11e9-9e03-0912dd56f8e1.png"},
{"name":"9-9","url":"https://user-images.githubusercontent.com/7369612/61700663-7eb0c580-ad6f-11e9-8513-713cb71341d3.png"},
{"name":"9-10","url":"https://user-images.githubusercontent.com/7369612/61700666-7eb0c580-ad6f-11e9-999e-be8c4298c56a.png"},
{"name":"10-1","url":"https://user-images.githubusercontent.com/7369612/61700669-7f495c00-ad6f-11e9-8fd9-892834b17fae.png"},
{"name":"10-2","url":"https://user-images.githubusercontent.com/7369612/61700672-7f495c00-ad6f-11e9-9ede-c3200be829ae.png"},
{"name":"10-3","url":"https://user-images.githubusercontent.com/7369612/61700675-7f495c00-ad6f-11e9-8b28-c3873de69cc9.png"},
{"name":"10-4","url":"https://user-images.githubusercontent.com/7369612/61700678-7fe1f280-ad6f-11e9-8c0e-505d6678f852.png"},
{"name":"10-5","url":"https://user-images.githubusercontent.com/7369612/61700680-7fe1f280-ad6f-11e9-9862-c4ba1b6c172d.png"},
{"name":"10-6","url":"https://user-images.githubusercontent.com/7369612/61700681-7fe1f280-ad6f-11e9-84f8-e543fc876b3a.png"},
{"name":"10-7","url":"https://user-images.githubusercontent.com/7369612/61700683-807a8900-ad6f-11e9-8457-6308ae01e8bf.png"},
{"name":"10-8","url":"https://user-images.githubusercontent.com/7369612/61700685-807a8900-ad6f-11e9-81bb-ad17ee0569e6.png"},
{"name":"10-9","url":"https://user-images.githubusercontent.com/7369612/61700686-81131f80-ad6f-11e9-9c1d-047fd1fca505.png"},
{"name":"10-10","url":"https://user-images.githubusercontent.com/7369612/61700688-81131f80-ad6f-11e9-9108-2a926d469ec1.png"}]
