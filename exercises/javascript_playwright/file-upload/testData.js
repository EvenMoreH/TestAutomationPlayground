export const testFiles = ["test_doc.txt", "test_doc2.txt", "test_doc3.txt"];

export const getFilePaths = (dir) => {
    return testFiles.map((file) => dir + file);
};
