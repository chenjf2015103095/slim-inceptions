window.onload = function() {
  Vue.prototype.$http = axios;
  var app = new Vue({
    el: '#app',
    data() {
      return {
        midImgList: [],
        closeImgList: [],
        currentList: [],
        currentType: 1,
        assessmentId: '',
        result: null,
        dropFlag: false,
        show:false,
        ai_result: null,
        ai_message: null,
      };
    },
    methods: {
      init() {
        this.midImgList = [];
        this.closeImgList = [];
        this.currentList = [];
        this.currentType = 1;
        this.assessmentId = '';
        this.result = null;
        this.dropFlag = false;
        this.ai_result = null;
        this.ai_message = null;
      },
      upLoadFIle(file) {
        let formData = new FormData();
        formData.append('picType', this.currentType);
        formData.append('fileUpload', file);
        formData.append('assessmentId', this.assessmentId);
        const config = {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        };
        const url = 'upload';
//        const url = 'https://test.lexiugo.com/web-ai/aiWeb/uploadPic';
        return this.$http.post(url, formData, config);
      },
      getResult() {
        this.show=true;
        let that = this;
        let formData = new FormData();
        formData.append('assessmentId', this.assessmentId);
        const config = {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        };
        const url = 'infer';
        this.$http.post(url, formData, config).then(function(res) {
          that.result = res.data.result;
          that.show=false;
        });
      },
      fileChange(el) {
        if (!el.target.files[0].size) return;
        this.fileList(el.target);
        el.target.value = '';
      },
      fileList(fileList) {
        let files = fileList.files;
        for (let i = 0; i < files.length; i++) {
          //判断是否为文件夹
          if (files[i].type != '') {
            this.fileAdd(files[i]);
          } else {
            //文件夹处理
            this.folders(fileList.items[i]);
          }
        }
      },
      //文件夹处理
      folders(files) {
        let _this = this;
        //判断是否为原生file
        if (files.kind) {
          files = files.webkitGetAsEntry();
        }
        files.createReader().readEntries(function(file) {
          for (let i = 0; i < file.length; i++) {
            if (file[i].isFile) {
              _this.foldersAdd(file[i]);
            } else {
              _this.folders(file[i]);
            }
          }
        });
      },
      foldersAdd(entry) {
        let _this = this;
        entry.file(function(file) {
          _this.fileAdd(file);
        });
      },
      fileAdd(file) {
        //总大小
        this.size = this.size + file.size;
        //判断是否为图片文件
        if (file.type.indexOf('image') == -1) {
          file.src = 'wenjian.png';
          this.currentList.push({
            file,
          });
        } else {
          let reader = new FileReader();
          reader.vue = this;
          let that = this;
          reader.readAsDataURL(file);
          reader.onload = function() {
            file.src = this.result;
            that.upLoadFIle(file).then(function(res) {
              if (res.data.data.code=='000') {
                that.ai_message=res.data.data.message;
                that.ai_result=res.data.data.result;
                setTimeout(() => {
                    document.getElementsByClassName('item-ai-message')[0].innerHTML = that.ai_message;
                    document.getElementsByClassName('item-ai-result')[0].innerHTML = that.ai_result;
                },100)

                that.dropFlag = true;
                that.show=false;
                that.currentList.push({
                  file,
                });
              } else {
                alert(res.data.data.message);
              }
            });
          };
        }
      },
      fileDel(index) {
        this.size = this.size - this.currentList[index].file.size; //总大小
        this.currentList.splice(index, 1);
      },
      bytesToSize(bytes) {
        if (bytes === 0) return '0 B';
        let k = 1000, // or 1024
          sizes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
          i = Math.floor(Math.log(bytes) / Math.log(k));
        return (bytes / Math.pow(k, i)).toPrecision(3) + ' ' + sizes[i];
      },
      dragenter(el) {
        el.stopPropagation();
        el.preventDefault();
      },
      dragover(el) {
        el.stopPropagation();
        el.preventDefault();
      },
      drop(el) {
        this.show=true;
        el.stopPropagation();
        el.preventDefault();
        if (el.target.id == 'midImg') {
          if (this.midImgList.length > 0) {
            this.init();
            this.currentList = this.midImgList;
            this.currentType = 1;
            this.fileList(el.dataTransfer);
//            if (
//              confirm(
//                '中景照只允许一张，您的当前操作会导致重新开始一次识别并清空当前数据，您确定继续操作吗?'
//              )
//            ) {
//              this.init();
//              this.currentList = this.midImgList;
//              this.currentType = 1;
//              this.fileList(el.dataTransfer);
//            } else {
//              return;
//            }
          }else{
            this.currentList = this.midImgList;
            this.currentType = 1;
            this.fileList(el.dataTransfer);
          }
        }
        if (el.target.id == 'closeImg') {
          if (this.dropFlag) {
            this.currentList = this.closeImgList;
            this.currentType = 2;
            this.fileList(el.dataTransfer);
          } else {
            alert('请先上传中景照');
          }
        }
      },
    },
  });
};
