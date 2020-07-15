<script>
import axios from 'axios'
import Alert from '../components/Alert.vue'
export default {
    components: {
        alert: Alert
    },
    data () {
        return {
            msg: [],
            addSthForm: {
                title: '',
                comment: '',
                check: [],
            },
            message: '',
            showMessage: false,
            editForm: {
                id: '',
                title: '',
                comment: '',
                check: [],
            },
        }
    },
    methods:{
        getSomething() {
            const url = 'http://localhost:5000/Sth';
            axios.get(url)
            .then((res) => {
                this.msg = res.data.something;
            })
            .catch((error) => {
                console.log(error);
            });
        },
        onSubmit() {
            console.log('onSubmit');
            this.$refs.addSthModal.hide();
            let check = false;
            if (this.addSthForm.check[0]) {check = true;}
            const data = {
                'title' : this.addSthForm.title,
                'comment' : this.addSthForm.comment,
                'check' : check
            }
            this.addForm(data);
            this.initForm();
        },
        onReset(evt) {
            console.log('onReset');
            evt.preventDefault();
            this.$refs.addSthModal.hide();
            this.initForm();
        },
        addForm(data) {
            console.log('addForm', data);
            const url = 'http://localhost:5000/Sth'
            axios.post(url, data)
            .then(() => {
                this.getSomething();
                this.message = 'Something added!';
                this.showMessage = true;
            })
            .catch((error) => {
                console.log(error);
                this.getSomething();
            })
        },
        initForm() {
            console.log('initForm');
            this.addSthForm.title = '';
            this.addSthForm.comment = '';
            this.addSthForm.check = [];

            this.editForm.id = '';
            this.editForm.title = '';
            this.editForm.comment = '';
            this.editForm.check = [];
        },
        editBook(seleted) {
            this.editForm = seleted;
            console.log(this.editForm)
        },
        onSubmitUpdate() {
            console.log('onSubmitUpdate');
            this.$refs.editSthModal.hide();
            let check = false;
            if (this.editForm.check[0]) {check = true;}
            const data = {
                'title' : this.editForm.title,
                'comment' : this.editForm.comment,
                'check' : check
            }
            this.updateSth(data, this.editForm.id)
        },
        updateSth(data, sthID) {
            const url = `http://localhost:5000/Sth/${sthID}`;
            axios.put(url, data)
            .then(() => {
                this.getSomething();
                this.message = 'Something updated!';
                this.showMessage = true;
            })
            .catch((error) => {
                console.log(error);
                this.getSomething();
            })
        },
        onResetUpdate() {
            this.$refs.editSthModal.hide();
            this.initForm();
            this.getSomething();
        },
        removeBook(sthID) {
            const url = `http://localhost:5000/Sth/${sthID}`;
            axios.delete(url)
            .then(() => {
                this.getSomething();
                this.message = 'Something removed!';
                this.showMessage = true;
            })
            .catch((error) => {
                console.log(error);
                this.getSomething();
            })
        },
        onDeleteBook(seleted) {
            this.removeBook(seleted.id);
        },
    },
    created() {
        this.getSomething();
    }

}
</script>

<template>
    <div>
        <h1>Record Something..</h1>
        <hr><br><br>
        <alert :message="message" v-if="showMessage"></alert>
        <button class="btn btn-success col-5" v-b-modal.sth-add-modal>Add</button>
        <br><br>
        <table class="table">
            <thead>
                <tr>
                    <th>Title</th>
                    <th>Comment</th>
                    <th>Check?</th>
                    <th>Option</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(m, index) in msg" :key="index">
                    <td>{{ m.title }}</td>
                    <td>{{ m.comment }}</td>
                    <td>
                        <span v-if="m.commentheck">YES</span>
                        <span v-else>NO</span>
                    </td>
                    <td>
                        <button class="btn btn-warning" v-b-modal.sth-update-modal @click="editBook(m)">Update</button>
                        <button class="btn btn-danger " @click="onDeleteBook(m)">Delete</button>
                    </td>
                </tr>
            </tbody>
            
        </table>
        {{msg}}
        <br>
        <tr>
            {{addSthForm}}
        </tr>
        <tr>
            {{editForm}}
        </tr>
        <!-- Add modal -->
        <b-modal ref="addSthModal" id="sth-add-modal" title="Add Something...." hide-footer>

            <!-- Two present way in submit/reset -->
            <b-form @reset="onReset" class="w-100">
                <b-form-group label="Title:">
                    <b-form-input type="text" v-model="addSthForm.title" placeholder="Enter title.." required>
                    </b-form-input>
                </b-form-group>

                <b-form-group label="Comment:">
                    <b-form-input type="text" v-model="addSthForm.comment" placeholder="Enter comment.." required>
                    </b-form-input>
                </b-form-group>

                <b-form-group>
                    <b-form-checkbox v-model="addSthForm.check" value="true">Check?</b-form-checkbox>
                </b-form-group>

                <b-button @click="onSubmit" variant="primary">Submit</b-button>
                <b-button type="reset" variant="danger">Reset</b-button>
            </b-form>
        </b-modal>

        <!-- Edit modal -->
        <b-modal ref="editSthModal" id="sth-update-modal" title="Update Something...." hide-footer>
            <b-form>
                <b-form-group label="Title:">
                    <b-form-input type="text" v-model="editForm.title" placeholder="Enter title.." required>
                    </b-form-input>
                </b-form-group>

                <b-form-group label="Comment:">
                    <b-form-input type="text" v-model="editForm.comment" placeholder="Enter comment.." required>
                    </b-form-input>
                </b-form-group>

                <b-form-group>
                    <b-form-checkbox v-model="editForm.check" value="true">Check?</b-form-checkbox>
                </b-form-group>

                <b-button @click="onSubmitUpdate" variant="primary">Update</b-button>
                <b-button @click="onResetUpdate" variant="danger">Cancel</b-button>
            </b-form>
        </b-modal>
    </div>
</template>

<style>

.btn {
    margin: 2px;
}
</style>