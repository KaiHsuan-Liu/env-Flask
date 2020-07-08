<template>
    <div>
        <h1>Record Something..</h1>
        <hr><br><br>
        <button class="btn btn-success col-5" v-b-modal.sth-modal>Add</button>
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
                        <span v-if="m.check">YES</span>
                        <span v-else>NO</span>
                    </td>
                    <td>
                        <button class="btn btn-warning ">Update</button>
                        <button class="btn btn-danger ">Delete</button>
                    </td>
                </tr>
            </tbody>
            
        </table>
        {{msg}}
        <br>
        {{addSthForm}}

        <b-modal ref="addSthModal" id="sth-modal" title="Add one Something...." hide-footer>
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
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data () {
        return {
            msg: [],
            addSthForm: {
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
                this.getSomething()
            })
            .catch((error) => {
                console.log(error)
                this.getSomething()
            })
        },
        initForm() {
            console.log('initForm');
            this.addSthForm.title = '';
            this.addSthForm.comment = '';
            this.addSthForm.check = [];
        }
    },
    created() {
        this.getSomething();
    }

}
</script>

<style>

.btn {
    margin: 2px;
}
</style>